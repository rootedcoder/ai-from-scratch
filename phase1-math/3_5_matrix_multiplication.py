def get_row(M, i):
  return M[i]

def get_column(M, j):
  return [M[i][j] for i in range(len(M))]

def dot_product(row, col):
  return sum(row[i] * col[i] for i in range(len(row)))

def matrix_multiply(A, B):
  rows_A = len(A)
  cols_B = len(B[0])

  if len(A[0]) != len(B):
    return "Error: Number of columns in A must equal number of rows in B to perform matrix multiplication."
  
  result = []
  for i in range(rows_A):
    row_result = []
    for j in range(cols_B):
      # Compute the dot product of the i-th row of A and the j-th column of B
      row_result.append(dot_product(get_row(A, i), get_column(B, j)))
    # Append the computed row to the result matrix
    result.append(row_result)
  return result

A = [
  [1, 2],
  [3, 4]
]
B = [
  [5, 6],
  [7, 8]
]
print(matrix_multiply(A, B))

W = [
  [0.1, 0.2, 0.3],
  [0.4, 0.5, 0.6],
]
X = [
  [1, 4],
  [2, 5],
  [3, 6]
]
print(matrix_multiply(W, X))

X = [
  [1, 2, 3],
  [4, 5, 6]
]
print(matrix_multiply(W, X))  # This will raise an error since W is 2x3 and X is 2x3, which cannot be multiplied.