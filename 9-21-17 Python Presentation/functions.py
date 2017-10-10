#!/usr/bin/env python3

from typing import List


def tostr(item):
    '''
    Converts the input to a string
    '''
    return str(item)

print(repr(tostr(1)))
input()


def tostr2(item: str) -> str:
    '''
    Converts the input to a string
    '''
    return str(item)

print(repr(tostr2(2)))
input()


def sum(*args: int) -> int:
    '''
    Returns the sum of the arguments
    '''
    s: int = 0
    for item in args:
        s += item
    return s

print(repr(sum(1, 2, 3)))
input()


def d(**kwargs):
    '''
    Returns a dictionary of the arguments
    '''
    return kwargs

print(repr(d(one=1, two=2, three=3)))
input()


def find(l: List[str], x: str, i: int = 0):
    '''
    Recursively finds x in list l
    Good example for why you'd use default arguments
    '''
    if i >= len(l):
        return -1
    elif l[i] == x:
        return i
    else:
        return find(l, x, i+1)

print(repr(find(['one', 'two', 'three'], 'four')))
