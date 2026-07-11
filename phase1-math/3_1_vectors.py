def vector_add(v1, v2):
  """Add two vectors together."""
  return [v1[i] + v2[i] for i in range(len(v1))]

def vector_scale(v, scalar):
  """Scale a vector by a fixed unit."""
  return [scalar * x for x in v]

v1 = [3, 2]
v2 = [1, 4]
print(vector_add(v1, v2))

scalar = 3
print(vector_scale(v1, scalar))

scalar = -1
print(vector_scale(v1, scalar))

scalar = 0
print(vector_scale(v1, scalar))

scalar = 2
v1 = [1, 1]
scaled_v1 = vector_scale(v1, scalar)

scalar = 3
v2 = [2, 0]
scaled_v2 = vector_scale(v2, scalar)
print(vector_add(scaled_v1, scaled_v2))