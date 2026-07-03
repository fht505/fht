def paginate(items, page, page_size):
    """Return the slice of `items` for 1-indexed `page` of `page_size`."""
    if page < 1 or page_size < 1:
        raise ValueError("page and page_size must be >= 1")
    start = (page - 1) * page_size
    end = start + page_size - 1
    return items[start:end]


def page_count(items, page_size):
    """Number of pages needed to show all of `items`."""
    if page_size < 1:
        raise ValueError("page_size must be >= 1")
    return (len(items) + page_size - 1) // page_size
