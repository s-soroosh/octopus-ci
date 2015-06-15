from time import sleep
from senza.aws import get_stacks
from senza.cli import get_stack_refs, get_region, delete
from ci.deployment import check_deleted

__author__ = 'soroosh'

import click

from ci import probe
from senza import cli


@click.command("probe")
@click.option('--host', required=True, help='Host name which you want to ping.')
@click.option('--port', required=True, help='Port number which you want to ping.')
@click.option('--retries', default=10, help='Number of retries. default: 10')
@click.option('--interval', default=1, help='Time interval between probes (In second). default 1 second')
def probe_cmd(host, port, retries, interval):
    probe.try_connect(host, port, retries, interval)


@click.command("delete")
@click.argument("app_name")
@click.argument("prefix")
@click.argument("version")
def delete_stack(app_name, prefix, version):
    version = version.replace(".", "")
    stack_ref = [app_name, prefix + version]
    stack_refs = get_stack_refs(stack_ref)
    if len(stack_refs) > 1:
        raise click.UsageError("Please pass just 1 stack reference")

    region = get_region(None)
    stacks = list(get_stacks(stack_refs, region))
    if len(stacks) == 0:
        return

    delete([], region, None, None)
    while not check_deleted(stacks[0], region):
        sleep(5)
    print("Stack removed successfully.")


@click.group()
def grp(): pass


grp.add_command(probe_cmd)
grp.add_command(delete_stack)


def main(): grp()


if __name__ == '__main__':
    main()