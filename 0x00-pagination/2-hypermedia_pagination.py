#!/usr/bin/env python3
"""Simple pagination function in python"""
import math


server = __import__('1-simple_pagination').Server


def get_hyper(page: int = 1, page_size: int = 10) -> dict:
    """A function that takes two args nd returns key:value pairs
    """
    assert isinstance(page, int) and page > 0
    assert isinstance(page_size, int) and page_size > 0

    # server = Server()
    dataset = server.dataset()

    start_index, end_index = index_range(page, page_size)

    if start_index >= len(dataset):
        return {
                "page_size": 0,
                "page": page,
                "data": [],
                "next_page": None,
                "prev_page": None,
                "total_pages": 0,
        }

    page_data = dataset[start_index:end_index]
    total_pages = math.ceil(len(dataset) / page_size)

    next_page = page + 1 if end_index < len(dataset) else None
    prev_page = page - 1 if start_index > 0 else None

    return {
            "page_size": len(page_data),
            "page": page,
            "data": page_data,
            "next_page": next_page,
            "prev_page": prev_page,
            "total_pages": total_pages,
    }
