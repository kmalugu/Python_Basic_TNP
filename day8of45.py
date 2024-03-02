# def printer(*args):
#     print(args)
# printer(1,2,3,"hello")


# def printer(*args, **kwargs):
#     print(f"args: {args} \nkargs: {kwargs}")
# printer(1,2,3,name="Karthik", age=21, dept="CSE")


# class Animal:
#     def shout(self):
#         print("Animal Shouting")
# class Dog(Animal):
#     def bark(self):
#         print("Dog Barking")
#
# d = Dog()
# d.bark()
# d.shout()




# Multi level Inheritance

class Animal:
    def shout(self):
        print("Animal Shouting")

class Dog(Animal):
    def bark(self):
        print("Dog Barking")

class Dog_breed(Dog):
    def breed(self):
        print("Breed Labrador")

    def bark(self):
        print("Labrador Barking")

d = Dog_breed()
d.breed()
d.bark()
d.shout()
