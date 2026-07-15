def get_shape(tensor):
  """Recursively determine the shape of a nested list"""

  if not (isinstance(tensor, list)):
    return ()
  
  return (len(tensor), ) + get_shape(tensor[0])

def broadcast_add_bias(M, b):
  """Add vector b to every row of matrix M."""
  return [[M[i][j] + b[j] for j in range(len(b))] for i in range(len(M))]

v = [1, 2, 3]
print(get_shape(v))

M = [
  [1, 2],
  [3, 4],
  [5, 6]
]
print(get_shape(M))

M = [
  [
    [1, 2],
    [3, 4],
  ],
  [
    [5, 6],
    [7, 8]
  ]
]
print(get_shape(M))

M = [
  [1, 2, 3],
  [4, 5, 6]
]
b = [10, 20, 30]
print(broadcast_add_bias(M, b))

b = [10, 20]
print(broadcast_add_bias(M, b))

# To test the Index out of range issue when running
# b = [10, 20, 30, 40]
# print(broadcast_add_bias(M, b))
