def most_frequent_element(data: list):
    return max(set(data), key=data.count)

print(most_frequent_element([1, 2, 3, 1, 2, 1]))
print(most_frequent_element(["a", "b", "a", "c", "a", "b"]))
print(most_frequent_element([7, 8, 8, 9, 7, 7, 8]))
