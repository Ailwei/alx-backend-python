#!/usr/bin/env python3
"""
function to_kv that takes a string k and an int OR
float v as arguments and returns a tuple.
The first element of the tuple is the string k.
The second element is the square of the int/float should be annotated  float.
"""


from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """Converts input to a tuple with the
    first element as string k and the second as the square of int/float v."""
    return (k, v ** 2.0)
