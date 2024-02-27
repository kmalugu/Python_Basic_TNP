# def printer(*args):
#     print(args)
# printer(1,2,3,"hello")


def printer(*args, **kwargs):
    print(f"args: {args} \nkargs: {kwargs}")
printer(1,2,3,name="Karthik", age=21, dept="CSE")
