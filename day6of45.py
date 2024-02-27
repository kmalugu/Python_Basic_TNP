# # O - Battery Low
#
# test_cases = int(input())
# for i in range(0,test_cases):
#     battery_level = int(input())
#     if battery_level <= 15:
#         print("Yes")
#     else:
#         print("No")



# P - Chef and Candies

test_cases = int(input())
for i in range(0,test_cases):
    child, candies = map(int,input().split())
    if child > candies:
        left = child - candies
        res = left % 4
        print(res)
    else:
        print(0)