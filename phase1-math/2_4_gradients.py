def f(x, y, n = 2):
  return x**n + y**n

def gradient(x, y, n, h=0.0001):
  """Returns the gradient of f(x, y) = x^n + y^n at the point (x, y)."""
  df_dx = (f(x + h, y, n) - f(x, y, n)) / h
  df_dy = (f(x, y + h, n) - f(x, y, n)) / h
  return [df_dx, df_dy]

def gradient_step(x, y, n, learning_rate=0.01, h=0.0001):
  """Performs a single gradient descent step for f(x, y) = x^n + y^n."""
  grad = gradient(x, y, n, h)
  new_x = x - learning_rate * grad[0]
  new_y = y - learning_rate * grad[1]
  return new_x, new_y


x = 3
y = 4
n = 2

print(gradient(x, y, n))
print(gradient_step(x, y, n))

for step in range(50):
  x, y = gradient_step(x, y, n)
  if(step % 10 == 0):
    print(f"Step {step}: x = {x}, y = {y}, f(x, y) = {f(x, y, n)}")