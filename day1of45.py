#assert keyword is used to debug the code
# It is used to check whether some part of the code is true or false

x = "hello"

#if condition is false, then we can print our output as AssertionError
assert x == "goodbye","x should be hello"



#raise keyword is used to raise an Exception

x = "hello"

if not type(x) is int:
    raise TypeError("x should be an integer")