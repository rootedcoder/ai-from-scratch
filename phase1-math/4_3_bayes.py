def bayes_theorem(p_a, p_b_given_a, p_b_given_not_a):
  p_not_a = 1 - p_a
  p_b = p_b_given_a * p_a + p_b_given_not_a * p_not_a
  p_a_given_b = (p_b_given_a * p_a) /p_b
  return p_a_given_b

p_a = 0.01
p_b_given_a = 0.95
p_b_given_not_a = 0.05
print(bayes_theorem(p_a, p_b_given_a, p_b_given_not_a))

p_a = 0.5
print(bayes_theorem(p_a, p_b_given_a, p_b_given_not_a))

p_a = 0.01
p_b_given_a = 0.6
print(bayes_theorem(p_a, p_b_given_a, p_b_given_not_a))