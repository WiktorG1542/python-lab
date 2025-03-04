def longest_increasing_subsequence(seq: list[int]):
  longest = 1

  current = 1
  for a in range (0, len(seq)-2):
    if (seq[a]<seq[a+1]):
      current = current + 1
    else:
      current = 1

    if (current>longest):
      longest = current

  return longest


print("longest_increasing_subsequence([1, 2, 3, 1, 2, 3, 4, 5, 1, 2, 3]):\n", longest_increasing_subsequence([1, 2, 3, 1, 2, 3, 4, 5, 1, 2, 3]))