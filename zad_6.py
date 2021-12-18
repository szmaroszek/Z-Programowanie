def add_lists(data1: list, data2: list) -> list:
    return [x**3 for x in list(set(data1 + data2))]


result = add_lists([1, 2, 3, 4, 5, 6], [20, 12, 23, 54, 5, 6])

print(result)
