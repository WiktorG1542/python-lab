def fibonacci_generator(n: int):

  if (n==1):
    return [1]
  elif (n==2):
    return [1, 1]
  else:
    l = [1, 1]
    for a in range(0, n-2):
      l.append(l[len(l)-1] + l[len(l)-2])

  return l


print("fibonacci_generator(5): ", fibonacci_generator(10))