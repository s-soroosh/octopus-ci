__author__ = 'soroosh'

import boto


def check_deleted(stack, region):
    cf = boto.cloudformation.connect_to_region(region)

    stacks = cf.list_stacks()
    non_deleted_stacks = list(
        filter(lambda s: s.stack_name == stack.stack.stack_name and s.stack_status != "DELETE_COMPLETE", stacks))
    if len(non_deleted_stacks) != 0:
        print("There are {0} non deleted stack".format(len(non_deleted_stacks)))
        return False

    return True

