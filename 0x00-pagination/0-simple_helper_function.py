#!/usr/bin/env python3
"""Pagination helper function.
"""


def index_range(page, page_size):
    """Retrieves the index range from a given page and page size.
    """
    start = (page - 1) * page_size
    end = page * page_size
    range_tuple = (start, end)
    return range_tuple

if __name__ == "__main__":
    res = index_range(1, 7)
    print(type(res))
    print(res)

    res = index_range(page=3, page_size=15)
    print(type(res))
    print(res)
