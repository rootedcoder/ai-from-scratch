import math

def underflow_computation():
  p = 0.01
  product = 1.0

  log_p = math.log(p)
  log_sum = 0.0

  for i in range(200):
    product *= p # will hit exactly 0.0 well before 200 iterations
    log_sum += log_p #stays a perfect meaningful, precise number the whole time

    if(i % 20 == 0): 
      print(f"{i}th iteration\nProduct: {product}, with Log: {log_sum}")
  
  return product, log_sum

def naive_difference(a, b):
  return a - b

def relative_error(approx, true_value):
  return abs(approx - true_value) / abs(true_value)

underflow_computation()

a = 1.0 + 1e-16
b = 1.0
print("Naive difference: ", naive_difference(a, b))
print("Relative Error Difference: ", relative_error(a, b))