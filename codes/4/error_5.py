# Python program to demonstrate finally
  
# No exception Exception raised in try block
try:
    k = 5//0  # raises divide by zero exception.
    print(k)
  
# handles zerodivision exception
except ZeroDivisionError:
    print("Can't divide by zero")
  
finally:
    # this block is always executed
    # regardless of exception generation.
    print('This is always executed')