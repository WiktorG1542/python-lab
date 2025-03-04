def round_numbers(numbers: list[int], threshold: int):
  l = []
  
  for n in numbers:
    if n < threshold:
      rounded = (n // 10) * 10
      l.append(rounded)
    else:
      rounded = ((n // 10) + 1) * 10
      l.append(rounded)

  return l

print("round_numbers([1, 2, 3, 4, 5, 6, 7, 8, 9], 5):\n", round_numbers([1, 2, 3, 4, 5, 6, 7, 8, 9], 5))
