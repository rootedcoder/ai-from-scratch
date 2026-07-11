def vector_dot_product(v1, v2):
  return sum(v1[i] * v2[i] for i in range(len(v1)))


def get_row(M, i):
  return M[i]

def matrix_vector_multiply(M, v):
  """
  Multiply a matrix by a vector.
    Rules for Multiplication:
      - The number of columns in the matrix must equal the number of rows in the vector.
      - For example, if M is a 2 x 3 matrix, then v must be a 3 x 1 vector.
  """
  return [vector_dot_product(get_row(M, i), v) for i in range(len(M))]


M = [
  [2, 1],
  [0, 4]
]
v = [
  3, 
  5
] # Represent as 2 rows and 1 column vector

print(matrix_vector_multiply(M, v))

# W represents a 2 x 3 matrix, and x represents a 3 x 1 vector. 
# The result of multiplying W by x will be a 2 x 1 vector.
W = [
  [0.1, 0.2, 0.3],
  [0.4, 0.5, 0.6],
]
x = [
  1, 
  2, 
  3
] # Represent as 3 rows and 1 column vector 

print(matrix_vector_multiply(W, x))