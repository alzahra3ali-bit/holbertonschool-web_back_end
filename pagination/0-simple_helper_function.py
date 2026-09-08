#!/usr/bin/env python3
def index_range(page, page_size):
    start_index = (page-1)*page_size
    end_index= page*page_size
    tuble = (start_index, end_index)
    return tuble
