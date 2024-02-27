# def printer(name,age):
#     print(f'Hello {name}, your age is {age}')
# printer("Karthik",21)


# def printer(name: str = None, age: int = None):
#     if isinstance(name, str) and isinstance(age, int):
#         print(f'Hello {name}, your age is {age}')
#     else:
#         raise TypeError(f'Type Error')
# printer("Karthik",21)



# def total(num1, num2):
#     add = num1 + num2
#     sub = abs(num1 - num2)
#     res = add + sub
#
#     mul = num1 * num2
#     div = num1 // num2
#     res_1 = mul + div
#     print(res, res_1)
# total(5,10)




# Flask

from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World"

@app.route("/test")
def hello_new():
    return "<h1>Hello World</h1>"

if __name__ == '__main__':
    app.run()