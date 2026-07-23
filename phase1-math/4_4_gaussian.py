import numpy as np

def generate_gaussian_samples(mean, std, n):
  return np.random.normal(loc=mean, scale=std, size=n) # reset the hidden global cursor to position "42"

def empirical_mean_std(samples):
  return samples.mean(), samples.std()

np.random.seed(42) # seed the generator # reset the hidden global cursor to position "42"

mean = 0
std = 1
n = 1000
samples = generate_gaussian_samples(mean, std, n)
print(empirical_mean_std(samples), samples.min(), samples.max())

mean = 100
std = 15
samples = generate_gaussian_samples(mean, std, n)
print(empirical_mean_std(samples), samples.min(), samples.max())

mean = 0
std = 10
samples = generate_gaussian_samples(mean, std, n)
print(empirical_mean_std(samples), samples.min(), samples.max())