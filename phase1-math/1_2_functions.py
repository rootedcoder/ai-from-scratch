# %%
def g(x):
  return 1/x

print(g(1))
print(g(0))  # This will raise a ZeroDivisionError

# %%
def h(x):
  return x**2 -4

if __name__ == "__main__": # To run the tests only when this file is executed directly
  print(h(2))
  print(h(-2))
  print(h(0))
