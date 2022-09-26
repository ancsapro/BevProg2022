def f():
    return 4 / 0


def g():
    raise Exception("Don't call us. We'll call you")


def h():
    try:

        f()

    except Exception as e:

        print(e)

    try:

        g()

    except Exception as e:

        print(e)

if __name__ == '__main__':
    h()