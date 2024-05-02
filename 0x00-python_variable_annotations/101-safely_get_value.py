#!/usr/bin/env python3
"""
Get a value safely from a dictionary.

    Parameters:
        dct (Dict[K, V]): The dictionary to look up.
        key (K): The key to look up in the dictionary.
        default (Optional[V], optional): The default value to return 
        if the key is not found. Defaults to None.

    Returns:
        Optional[V]: The value associated with the key if found,
        or the default value if the key is not found.
"""


from typing import TypeVar, Dict, Optional

K = TypeVar('K')  # Placeholder for dictionary keys
V = TypeVar('V')  # Placeholder for dictionary values

def safely_get_value(dct: Dict[K, V], key: K, default: Optional[V] = None) -> Optional[V]:
    """
    Duck-typed annotation
    """
    if key in dct:
        return dct[key]
    else:
        return default
