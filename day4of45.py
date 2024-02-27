# # A - Write a program which prints 1000 "Hello World".
#
# for i in range(1,1001):
#     print("Hello World")
#
#
# # B - Write a program which prints small/large/equal relation of given two integers a and b.
# a,b = [int(i) for i in input().split()]         # List Comprehension
# if a>b:
#     print("a > b")
# elif a<b:
#     print("a < b")
# else:
#     print("a == b")
#
#
# # C - Given the length and breadth of a rectangle, print area of the rectangle.
#
# l,b = [int(i) for i in input().split()]
# area = l * b
# print(area)
#
#
# # D - Given the length of 3 sides of a triangle, check whether the triangle is valid or not.
# a,b,c = [int(i) for i in input().split()]
# a_sq = a**2
# b_sq = b**2
# c_sq = c**2
# if (a_sq+b_sq == c_sq):
#     print("Yes")
#
#
#
# # E - Find the missing number in the given list of integers.
# # The list contains 1 to 100 integers but one of the integer is missing.
# # There are no duplicates in the list.
#
# list_1 = list(map(int,input().split()))
# for i in range(1,100):
#     if i not in list_1:
#         print(i)
#
#
#
# # F - Given a number N, reverse the number.
#
# num = int(input())
# sum = 0
# while num>0:
#     digit = num % 10
#     sum = sum*10 + digit
#     num //= 10
# print(sum)
#
#
#
# # G - n schoolchildren divide k apples evenly, the residue remains in the basket.
# # How many apples remains in the basket?
#
# child = int(input())
# apples = int(input())
# print(apples%child)



# H - Watermelon

weight_watermelon = int(input())
if weight_watermelon % 2 == 0:
    print("YES")
    list_2 = []
    for i in range(1,weight_watermelon):
        if i % 2 == 0:
            list_2.append(i)
    for i in list_2:
        j = i + 2
        for j in list_2:
            if i + j == weight_watermelon:
                print(i,j)
else:
    print("NO")
