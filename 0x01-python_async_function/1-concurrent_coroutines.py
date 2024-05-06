#!/usr/bin/env python3
"""
Asynchronous routine that spawns wait_random n times with
the specified max_delay.
"""

import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int = 10) -> List[float]:
    """
      List[float]: The list of all the delays in ascending order.
    """

    delays = []
    tasks = [wait_random(max_delay) for _ in range(n)]

    for tasks in asyncio.as_completed(tasks):
        delay = await tasks
        delays.append(delay)

    return delays
