#!/usr/bin/env python3
"""
write a coroutine called async_comprehension that takes no arguments.
"""


from typing import List
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """
    Coroutine that collects 10 random numbers using async comprehension
    """
    
    return [number async for number in async_generator()]
