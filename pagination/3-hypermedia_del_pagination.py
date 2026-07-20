#!/usr/bin/env python3
"""
Deletion-resilient hypermedia pagination
"""

import csv
import os
from typing import Any, Dict, List


class Server:
    """Server class to paginate a database of popular baby names."""
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset."""
        if self.__dataset is None:
            if not os.path.exists(self.DATA_FILE):
                raise FileNotFoundError(f"{self.DATA_FILE} not found.")
            with open(self.DATA_FILE, newline="") as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]
        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """Dataset indexed by position, starting at 0."""
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }
        return self.__indexed_dataset

    def get_hyper_index(
        self,
        index: int = None,
        page_size: int = 10,
    ) -> Dict[str, Any]:
        """
        Return a dictionary with pagination data resilient to deletions.
        """
        indexed_data = self.indexed_dataset()
        dataset_size = len(indexed_data)

        if index is None:
            index = 0
        elif not isinstance(index, int):
            raise TypeError("index must be an integer")
        elif index < 0:
            raise ValueError("index must be non-negative")
        elif index > dataset_size:
            return {
                "index": index,
                "data": [],
                "page_size": 0,
                "next_index": None,
            }

        if not isinstance(page_size, int):
            raise TypeError("page_size must be an integer")
        if page_size <= 0:
            raise ValueError("page_size must be positive")

        data = []
        current_index = index

        while len(data) < page_size and current_index < dataset_size:
            item = indexed_data.get(current_index)
            if item is not None:
                data.append(item)
            current_index += 1

        next_index = current_index if current_index < dataset_size else None

        return {
            "index": index,
            "data": data,
            "page_size": len(data),
            "next_index": next_index,
        }
