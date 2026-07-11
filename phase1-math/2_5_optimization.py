def f(x):
  return x**4 - 4 * x**2

def derivative(x, h=0.0001):
  return (f(x + h) - f(x)) / h

def gradient_descent_1d(x_start, steps=100, learning_rate=0.01):
  x = x_start
  
  for step in range(steps):
    grad = derivative(x)
    x = x - learning_rate * grad

  return x
  

print(gradient_descent_1d(1.5))
print(gradient_descent_1d(-1.5))
print(gradient_descent_1d(0.01))
print(gradient_descent_1d(0))