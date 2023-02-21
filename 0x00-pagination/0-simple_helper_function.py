#!/usr/bin/env python3
"""A simple helper pagination function in python"""


def index_range(page: int, page_size: int) -> tuple:
    """A function that returns the start and end index for pagination
    Args:
        Page -> integer indicating the first page
        page_size -> integer indicating the number of pages to load/release"""
    start_index = (page - 1) * page_size
    end_index = page * page_size
    return (start_index, end_index)
