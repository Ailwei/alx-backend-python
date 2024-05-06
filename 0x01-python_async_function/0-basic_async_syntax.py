#!/usr/bin/env python3
import asyncio
import random


"""
asynchronous coroutine that takes in an integer argument
named wait_random that waits for a random delay between 0 and max_delay
"""


async def wait_random(max_delay: int = 10) -> float:
    """
      Asynchronous coroutine that waits for a random delay
    """

    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
