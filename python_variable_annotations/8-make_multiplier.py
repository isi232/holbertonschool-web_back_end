#!/usr/bin/env python3
"""Module that provides a function returning a float multiplier function."""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """Return a function that multiplies a float by the given multiplier."""
    def multiply(x: float) -> float:
        """Multiply x by the outer multiplier and return the result."""
        return x * multiplier
    return multiply
