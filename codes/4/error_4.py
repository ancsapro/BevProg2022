def fun(a):
    if a < 4:
        # throws ZeroDivisionError for a = 3
        b = a / (a - 3)

    # throws NameError if a >= 4

    print("Value of b = ", b)


try:
    fun(3)
    fun(5)

# note that braces () are necessary here for
# multiple exceptions

except ZeroDivisionError:
    print("ZeroDivisionError Occurred and Handled")
except NameError:
    print("NameError Occurred and Handled")