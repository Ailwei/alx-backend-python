#!/usr/bin/env python3
"""Given the parameters and the return values, add type
annotations to the function

Hint: look into TypeVar

def safely_get_value(dct, key, default = None):
    if key in dct:
        return dct[key]
    else:
        return default
"""


import typing


T = typing.TypeVar('T')


def safely_get_value(dct: typing.Mapping[typing.Any, T], key: typing.Any,
                     default: typing.Optional[T] = None) -> typing.Union[T, typing.Any]:
    """annotations of the function"""
    if key in dct:
        return dct[key]
    else:
        return default
