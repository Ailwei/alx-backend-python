#!/usr/bin/env python3
"""
 a coroutine called async_generator that takes no arguments
"""


import asyncio
import random


async def async_generator():
    """Coroutine that generates random numbers asynchronously."""
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.randint(0, 10)
