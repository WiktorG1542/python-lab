def prime_selector(numbers: list[int]):
  primeList = []

  for n in numbers:
    if (is_it_prime(n)):
      primeList.append(n)

  return primeList


def is_it_prime(n):
  if (n<=1):
    return False

  for a in range(2, int(n/2)+1):
    if (n%a==0):
      return False

  return True


l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
print("list: ", l)
print("prime_selector(l): ", prime_selector(l))