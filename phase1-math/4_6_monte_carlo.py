import numpy as np

def estimate_pi(n_samples):
  x = np.random.uniform(-1, 1, n_samples)
  y = np.random.uniform(-1, 1, n_samples)
  inside_circle = (x**2 + y**2) <= 1
  fraction_inside = inside_circle.sum()  / n_samples
  return 4 * fraction_inside

print(estimate_pi(n_samples=1000))
print(estimate_pi(n_samples=100000))

print(estimate_pi(n_samples=1000))
print(estimate_pi(n_samples=1000))
print(estimate_pi(n_samples=1000))