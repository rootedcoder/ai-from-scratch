import numpy as np

def solve_linear_systems(_A, _b):
  """Returns x from A.x = b (Similar to linear algebra 2x = 8)"""
  A = np.array(_A)
  b = np.array(_b)

  x = np.linalg.solve(A, b)
  return x

# For two equations, A & B are below
# Eq. 1: 2x + y = 11 => A[0] = [2,  1] (Coefficients/Prefix nos of x & y which is 2 &  1), b[0] = 11
# Eq. 2:  x - y =  1 => A[1] = [1, -1] (Coefficients/Prefix nos of x & y which is 1 & -1), b[1] = 1
A = [
  [2, 1],
  [1, -1]
]
b = [11, 1]
print(solve_linear_systems(A, b))
 
# Exercise 2
# Eq. 1: 3x + 2y = 12 => A[0] = [3,  2], b[0] = 12
# Eq. 2:  x -  y =  1 => A[1] = [1, -1], b[1] =  1
A = [
  [3, 2],
  [1, -1]
]
b = [12, 1]
print(solve_linear_systems(A, b))

# trying to check if det(A) = 0, what happens when solving the linear systems
# A = [
#   [2, 4],
#   [1, 2]
# ]
# b = [10, 5]
# print(solve_linear_systems(A, b))