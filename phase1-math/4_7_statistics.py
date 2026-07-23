import numpy as np

def generate_gaussian_samples(mean, std, n):
  return np.random.normal(loc=mean, scale=std, size=n) # reset the hidden global cursor to position "42"

def confidence_interval_95(samples):
  mean = samples.mean()
  std = samples.std()
  n = len(samples)
  std_error = std / np.sqrt(n)
  margin = 1.96 * std_error
  lower_interval = mean - margin
  upper_interval = mean + margin
  confidence_interval_width = upper_interval - lower_interval
  return lower_interval, upper_interval, confidence_interval_width

np.random.seed(42)
samples = generate_gaussian_samples(mean=0, std=1, n=1000)
print(confidence_interval_95(samples))

np.random.seed(43)
samples = generate_gaussian_samples(mean=0, std=1, n=100)
print(confidence_interval_95(samples))

np.random.seed(44)
samples = generate_gaussian_samples(mean=0, std=1, n=10000)
print(confidence_interval_95(samples))