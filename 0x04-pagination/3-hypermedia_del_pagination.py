#!/usr/bin/env python3
"""
Deletion-resilient hypermedia pagination"""

import csv
import math
from typing import List, Dict


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """Dataset indexed by sorting position, starting at 0
        """
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            truncated_dataset = dataset[:1000]
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict:
        """Return dict of pagination data.
        Args:
            index (int, optional): index. Defaults to None.
            page_size (int, optional): size of page. Defaults to 10.
        Returns:
            Dict: indexed data
        """
        len_data = len(self.dataset())
        assert 1 < index < len_data

        indexed_dataset = self.indexed_dataset()
        indexed_pages = {}
        for i in range(index, len_data):
            if i in indexed_dataset and len(indexed_pages) < page_size:
                indexed_pages[i] = indexed_dataset[i]
        pages = list(indexed_pages.values())
        idx = indexed_pages.keys()
        indexed_data = {
            'index': index,
            'data': pages,
            'page_size': len(pages),
            'next_index': max(idx) + 1
        }
        return indexed_data
