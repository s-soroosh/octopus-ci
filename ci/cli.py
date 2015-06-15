__author__ = 'soroosh'

import click

from ci import probe





@click.command("probe")
@click.option('--host', required=True, help='Host name which you want to ping.')
@click.option('--port', required=True, help='Port number which you want to ping.')
@click.option('--retries', default=10, help='Number of retries. default: 10')
@click.option('--interval', default=1, help='Time interval between probes (In second). default 1 second')
def probe_cmd(host, port, retries, interval):
    probe.try_connect(host, port, retries, interval)


@click.group()
def cli(): pass

cli.add_command(probe_cmd)

def main(): cli()


if __name__ == '__main__':
    main()