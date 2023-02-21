#!/usr/bin/env python3
""" """


def index_range(page: int, page_size: int) -> tuple:
    """"""
    start_index = page + page_size + 1
    end_index = start_index + page_size
    return (start_index, end_index)
