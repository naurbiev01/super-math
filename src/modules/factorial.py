def factorial_rec(n):
    if n <= 1:
        return 1
    return n * factorial_rec(n - 1)


def fact_normal(n):
  summa = 1
  for i in range(1, n + 1):
    summa += 1
  return summa
