def mean(data):
  return sum(data) / len(data)

def variance(data):
  m = mean(data)
  squred_diffs = [(x-m)**2 for x in data]
  return sum(squred_diffs) / len(data)

def std_dev(data):
  return variance(data) ** 0.5

data = [2, 4, 4, 4, 5, 5, 7, 9]
print('data=', data)
print('mean=', mean(data))
print('variance=', variance(data))
print('standard_deviation=', std_dev(data))

data = [3, 4, 5, 6, 7]
print('data=', data)
print('mean=', mean(data))
print('variance=', variance(data))
print('standard_deviation=', std_dev(data))

data = [5, 5, 5, 5, 5]
print('data=', data)
print('mean=', mean(data))
print('variance=', variance(data))
print('standard_deviation=', std_dev(data))