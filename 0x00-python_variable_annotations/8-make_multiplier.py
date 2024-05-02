#!/usr/bin/env python3


from typing import Callable


"""
type-annotated function make_multiplier that takes a float
multiplier as argument and returns a function that times a float by multipier.
"""



def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """Returns a function that multiplies a float by the given multiplier."""
    def multiplier_function(x: float) -> float:
        return x * multiplier
    return multiplier_function
