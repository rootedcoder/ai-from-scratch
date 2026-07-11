def matrix_shape(M):
  """Returns shape of the Matrix as rows, columns"""
  rows = len(M)
  columns = len(M[0])
  return rows, columns

W = [
  [0.1, 0.2, 0.3],
  [0.4, 0.5, 0.6],
]

print(matrix_shape(W))

def get_row(M, i):
  return M[i]

def get_column(M, j):
  return [M[i][j] for i in range(len(M))]

print(get_row(W, 0))
print(get_column(W, 1))