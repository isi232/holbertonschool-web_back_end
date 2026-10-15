#!/usr/bin/env python3
"""Hypermedia pagination."""
import csv
import math
from typing import Dict, List, Tuple


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


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """Return the requested page of the dataset.

        Args:
            page: page number (1-indexed), must be a positive int.
            page_size: items per page, must be a positive int.

        Returns:
            The list of rows for the page, or an empty list if the
            page is out of range.
        """
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0

        start, end = index_range(page, page_size)
        data = self.dataset()

        if start >= len(data):
            return []

        return data[start:end]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict:
        """Return a dictionary with hypermedia pagination info.

        Args:
            page: page number (1-indexed), must be a positive int.
            page_size: items per page, must be a positive int.

        Returns:
            A dictionary with page_size, page, data, next_page,
            prev_page and total_pages.
        """
        data = self.get_page(page, page_size)
        total_pages = math.ceil(len(self.dataset()) / page_size)

        return {
            "page_size": len(data),
            "page": page,
            "data": data,
            "next_page": page + 1 if page < total_pages else None,
            "prev_page": page - 1 if page > 1 else None,
            "total_pages": total_pages,
        }
