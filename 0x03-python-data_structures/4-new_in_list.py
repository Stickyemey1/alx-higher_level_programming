#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    myNewlist = my_list.copy()

    if idx < 0 0r idx >= len(my_list):
        return (myNewlist)

    myNewlist[idx] =element
    return (myNewlist)

