def zero():
    try:
        5/0
    except ZeroDivisionError:
        print("Can't divide by zero")

zero()