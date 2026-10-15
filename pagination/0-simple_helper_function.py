#!/usr/bin/env python3
"""Simple helper function for pagination."""
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """Return a tuple of start and end indexes for the given page.

    Args:
        page: page number (1-indexed).
        page_size: number of items per page.

    Returns:
        A tuple (start_index, end_index).
    """
    start = (page - 1) * page_size
    end = page * page_size
    return (start, end)
