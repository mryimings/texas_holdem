import sys

# Permutation from y to x.
# e.g. p(5,3) means 5*4*3.
def p(x, y):
  if x <= y:
    return y
  return x * p(x-1, y)

# Combination of y from x.
# e.g. c(5,3) means (5*4*3) / (3*2*1) 
def c(x, y):
  m = p(x, x-y+1)
  n = p(y, 1)
  return m / n

# Shortcut to get command line arguments
def g(x):
  return int(sys.argv[x])

# Usage: python calc.py <x1> <y1> <x2> <y2>
# Return: c(x1, y1) / c(x2, y2)
#
# Example: python calc.py 2 1 5 1
# Return: c(2,1) / c(5,1) = 2 / 5 = 0.4
if __name__ == '__main__':
  assert len(sys.argv) == 5
  m = c(g(1), g(2))
  n = c(g(3), g(4))

  print("Possibility of this event: ", m / n)
  print("Possibility of opposite event: ", 1 - m / n)
