#!/usr/bin/env python3
"""
Annotate the below function’s parameters and return
values with theappropriate types
"""


from typing import List, Tuple

def element_length(lst: List[str]) -> List[Tuple[str, int]]:
    """
     function’s parameters and return values with the appropriate
    """
    return [(i, len(i)) for i in lst]
