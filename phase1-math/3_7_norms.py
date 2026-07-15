import math

def dot_product(v1, v2):
  return sum(v1[i] * v2[i] for i in range(len(v1)))

def l1_norm(v):
  return sum(abs(x) for x in v)

def l2_norm(v):
  return math.sqrt(sum(x**2 for x in v))

def eucledian_distance(a, b):
  diff = [a[i] - b[i] for i in range(len(a))]
  return l2_norm(diff)

def cosine_similarity(a, b):
  return dot_product(a, b) / (l2_norm(a) * l2_norm(b))

v = [3, 4]
print(l1_norm(v))
print(l2_norm(v))

v1 = [3, 4]
v2 = [1, 2]
print(eucledian_distance(v1, v2))
print(cosine_similarity(v1, v2))

v1 = [3, 4]
v2 = [6, 8]
print(cosine_similarity(v1, v2))