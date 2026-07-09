def f(x):
  return x**2

def numeric_derivative(f, x, h=0.0001):
  return (f(x + h) - f(x)) / h

x = 3
print(numeric_derivative(f, x))

x = 0
print(numeric_derivative(f, x))

x = -2
print(numeric_derivative(f, x))

x = 3
print(numeric_derivative(f, x, h=0.00000001))