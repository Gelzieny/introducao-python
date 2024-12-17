def fatorial(n: int) -> int:
  #Caso base
  if n == 0 or n == 1:
    return 1
  
  return n * fatorial(n - 1)


def fibonacci(n):
  if n <= 0:  # Caso base
      return 0
  elif n == 1:
      return 1
  return fibonacci(n - 1) + fibonacci(n - 2)

if __name__ == "__main__":
  # fat5 = fatorial(10)
  fat5 = fibonacci(6)

  print(fat5)