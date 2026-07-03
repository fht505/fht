from pagination import paginate, page_count

items = list(range(10))

assert paginate(items, 1, 3)[0] == 0
assert paginate(items, 2, 3)[0] == 3
assert len(paginate(items, 1, 3)) <= 3
assert page_count(items, 3) == 4
assert page_count([], 3) == 0

print("visible tests passed")
