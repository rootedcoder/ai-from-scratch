def dot_product(row, col):
  return sum(row[i] * col[i] for i in range(len(row)))

def get_row(M, i):
  return M[i]

def matrix_vector_multiply(M, v):
  return [dot_product(get_row(M, i), v) for i in range(len(M))]

def check_eigenvector(M, v):
  result = matrix_vector_multiply(M, v)
  # If v is an eigenvector of M, (then Mv = λv for some scalar λ.), result should equal some scalar * v
  # Check by comparing ratios of corresponding components of result and v
  ratios = [result[i] / v[i] for i in range(len(v)) if v[i] != 0]
  if(all(abs(r - ratios[0]) < 1e-9 for r in ratios)):
    return True, ratios[0]  # Return True and the eigenvalue
  return False, None  # Not an eigenvector

M = [
  [2, 0],
  [0, 1]
]
v = [
  1,
  0
]
print(check_eigenvector(M, v))  # Should return (True, 2.0) since Mv = 2v

v = [
  1,
  1
]
print(check_eigenvector(M, v))  # Should return (False, None) since Mv != λv for any scalar λ

M = [
  [0, 1],
  [1, 0]
]
v = [
  1,
  1
]
print(check_eigenvector(M, v))  # Should return (True, 1.0) since Mv = 1v

v = [
  1, 
  -1
]
print(check_eigenvector(M, v))