from itertools import permutations

def unique_permutations(elements: list):
    return list(set(permutations(elements)))

print(unique_permutations([1, 2, 2]))  
print(unique_permutations(["a", "b", "a"]))  
print(unique_permutations([3, 3, 3]))  
