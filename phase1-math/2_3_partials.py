def f(x, y, n):
  return x**n + y**n

def partial_derivative_x(x, y, n=1, h=0.0001):
  return (f(x + h, y, n) - f(x, y, n)) / h

def partial_derivative_y(x, y, n=1, h=0.0001):
  return (f(x, y + h, n) - f(x, y, n)) / h

x = 3
y = 4
n = 2
print(partial_derivative_x( x, y, n), partial_derivative_y( x, y, n))

def f_multipy(x, y):
  return x * y

def partial_derivative_multiply_x(x, y, h=0.0001):
  return (f_multipy(x + h, y) - f_multipy(x, y)) / h

def partial_derivative_multiply_y(x, y, h=0.0001):
  return (f_multipy(x, y + h) - f_multipy(x, y)) / h

print(partial_derivative_multiply_x(x, y), partial_derivative_multiply_y(x, y))

def f_three_variables(x, y, z, n=1):
  return x**n + y**n + z**n

def partial_derivative_three_variables_x(x, y, z, n=1, h=0.0001):
  return (f_three_variables(x + h, y, z, n) - f_three_variables(x, y, z, n)) / h

def partial_derivative_three_variables_y(x, y, z, n=1, h=0.0001):
  return (f_three_variables(x, y + h, z, n) - f_three_variables(x, y, z, n)) / h

def partial_derivative_three_variables_z(x, y, z, n=1, h=0.0001):
  return (f_three_variables(x, y, z + h, n) - f_three_variables(x, y, z, n)) / h

z = 5
print(partial_derivative_three_variables_x(x, y, z, n), partial_derivative_three_variables_y(x, y, z, n), partial_derivative_three_variables_z(x, y, z, n))
