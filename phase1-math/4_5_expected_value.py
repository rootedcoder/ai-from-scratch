def compute_expected_value(outcome, probability):
  """Method to compute this - if I repeated this random process many, many times, what would the average outcome be?"""
  return sum(outcome[i] * probability[i] for i in range(len(outcome)))

outcome = [1, 2, 3, 4, 5, 6]
probability = [1/6, 1/6, 1/6, 1/6, 1/6, 1/6]
print(compute_expected_value(outcome, probability))

outcome = [10, 2, -5]
probability = [0.2, 0.5, 0.3]
print(compute_expected_value(outcome, probability))

probability = [0.1, 0.4, 0.5]
print(compute_expected_value(outcome, probability))