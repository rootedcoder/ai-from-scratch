def power_rule(n):
  """Returns the exponent multiplier and new exponent for f(x) = x^n."""
  return n, n - 1

def f_exponent(x, n):
  return x**n

def f_exponent_derivative(x, n):
  multiplier, new_exponent = power_rule(n)
  return multiplier * (x ** new_exponent)

def numeric_derivative(f, x, h=0.0001):
  return (f(x + h) - f(x)) / h

x = 3
n = 3
print(f_exponent_derivative(x, n), numeric_derivative(lambda x: f_exponent(x, n), x))


def f_chain_inner(x):
  return 2 * x + 3

def f_chain_inner_derivative(x):
  return 2

def f_chain_function(x):
  return f_chain_inner(x) ** 2

def f_chain_rule(x):
  """Returns the derivative of f(x) = (2x + 3)^2 using the chain rule."""
  inner_function = f_chain_inner(x)
  multiplier, new_exponent = power_rule(2)
  outer_function_derivative = multiplier * (inner_function ** new_exponent)
  inner_function_derivative = f_chain_inner_derivative(x)
  return outer_function_derivative * inner_function_derivative

x = 3

print(f_chain_rule(x), numeric_derivative(f_chain_function, x))


x = 3
print(f_exponent_derivative(x, 1))