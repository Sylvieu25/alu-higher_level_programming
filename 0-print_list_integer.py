#!/usr/bin/python3
def print_list_integer(my_list=[]):
    """Print all integers of a list, one per line."""
    for i in my_list:
        if isinstance(i, int):
            print("{:d}".format(i))
        else:
            raise TypeError("List must contain only integers")
