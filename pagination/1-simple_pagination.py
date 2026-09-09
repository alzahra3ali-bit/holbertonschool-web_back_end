#!/usr/bin/env python3
import csv
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    Calculate start and end indexes for a given page and page_size.
    """
    start_index = (page - 1) * page_size
    end_index = page * page_size
    tupl = (start_index, end_index)
    return tupl
    
import csv
import math
from typing import List


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

    def get_page(page=1, page_size=10 ) -> Tuple[int, int]:
        assert (isinstance(page, int) and isinstance(page_size, int)), "Page and page_size must be positive integers."
        assert (page > 0 and page_size > 0), "Page and page_size must be positive integers."
        start, end = index_range(page, page_size)
        data = self.dataset()
        if start >= len(data):
            return[]
            return data[start:end]
