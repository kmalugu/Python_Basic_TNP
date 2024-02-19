#raise keyword is used to raise an Exception

x = "hello"

if not type(x) is int:
    raise TypeError("x should be an integer")