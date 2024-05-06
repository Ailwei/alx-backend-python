#!/usr/bin/env python3
"""
Create an asyncio.Task for wait_random coroutine with the  max_delay
"""


import asyncio
from typing import Callable
wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """
     asyncio.Task: The Task object representing the
     execution of wait_random coroutine.
    """

    # Create a coroutine object
    coroutine = wait_random(max_delay)
    # Create and return an asyncio.Task object
    return asyncio.create_task(coroutine)
