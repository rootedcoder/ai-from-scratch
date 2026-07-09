def line(x, m, b):
  return m * x + b

def slope(x1, y1, x2, y2):
  return (y2 - y1) / (x2 - x1)

m = 2
b = 3

# Graph calculations for line = 2x + 3
x1 = 0
y1 = line(0, m, b)
print(x1, y1)

x2 = 1
y2 = line(1, m, b)
print(x2, y2)

x3 = 2
y3 = line(2, m, b)
print(x3, y3)

x4 = 3
y4 = line(3, m, b)
print(x4, y4)

x5 = 4
y5 = line(4, m, b)
print(x5, y5)

# Slope calculations for points (x2, y2) and (x5, y5)
slope_between = slope(x2, y2, x5, y5)
print(slope_between)  # Should print 2, which is the slope of the line

if(slope_between == m):
  print("Slope between points matches the slope of the line." + str(slope_between))

# Custom slope and y-intercept for a different line
m = -5
b = 5

y1 = line(x1, m, b)
print(x1, y1)

y2 = line(x2, m, b)
print(x2, y2)

y3 = line(x3, m, b)
print(x3, y3)
