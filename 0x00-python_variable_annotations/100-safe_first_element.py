#!/usr/bin/env python3

"""
 following code with the correct duck-typed annotations
"""
from typing import List, Any, Union


def safe_first_element(lst: List[Any]) -> Union[Any, None]:
    """Return the first element of a list if it exists, else None."""
    if lst:
        return lst[0]
    else:
        return None
