#!/usr/bin/env python3
"""Simple helper function for pagination"""
from typing import Tuple
"""
    Calculate start and end indexes for a given page and page_size.
"""
def index_range(page: int, page_size: int) -> Tuple[int,int]:
    start_index= (page-1)*page_size
    end_index= page*page_size
    tuple = (start_index, end_index)
    return tuple
