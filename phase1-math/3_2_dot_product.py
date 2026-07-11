def dot_product(v1, v2):
  """Compute the dot product of two vectors."""
  return sum(v1[i] * v2[i] for i in range (len(v1)))

v1 = [3, 4]
v2 = [1, 2]
print(dot_product(v1, v2))

v2 = [-3, -4]
print(dot_product(v1, v2))

v2 = [4, -3]
print(dot_product(v1, v2))


v1 = [10, 15, 20]
v2 = [12.5, 17.5, 22.5]
print(dot_product(v1, v2))

def vector_add(v1, v2):
  """Add two vectors together."""
  return [v1[i] + v2[i] for i in range(len(v1))]

def vector_scale(v, scalar):
  """Scale a vector by a fixed unit."""
  return [scalar * x for x in v]

v1 = [2, 3]
v2 = [1, 1]
print(vector_add(vector_scale(v1, 1), vector_scale(v2, 0)))