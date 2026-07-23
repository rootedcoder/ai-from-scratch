import math

def probability(favorable, total):
  return favorable / total

def independent_and(p_a, p_b):
  return p_a * p_b

def combinations(n, k):
  return math.factorial(n) / (math.factorial(k) * math.factorial(n - k))

# 1 represents rolling 4 in the dice with 6 faces
print(probability(1, 6))

# 0.5 represents getting heads in a coin toss of 2 sides, which is 1/2
# Flipping two coins simultaneously and checking the probability of getting heads in both coins combined
print(independent_and(0.5, 0.5))

# Flipping three coins
print(independent_and(0.5, independent_and(0.5, 0.5)))

# combinations
# getting 2 items from the list of 4
# Eg. {A, B, C, D}, combinations are [AB, AC, AD, BC, BD, CD] = 6
print(combinations(4, 2))

# Chooing 3 items from list of 6
print(combinations(6, 3))

# Choosing n from n list
print(combinations(5, 5))