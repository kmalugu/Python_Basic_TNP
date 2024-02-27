# # I - Fever
#
# test_cases = int(input())
# for i in range(0,test_cases):
#     temp = int(input())
#     if temp > 98:
#         print("YES")
#     else:
#         print("NO")



# # J - Lunchtime
#
# test_cases = int(input())
# for i in range(0,test_cases):
#     time = int(input())
#     if (time >= 1 and time <= 4):
#         print("YES")
#     else:
#         print("NO")


# # K - Is it hot or cold
#
# test_cases = int(input())
# for i in range(0,test_cases):
#     temp = int(input())
#     if temp>20:
#         print("HOT")
#     else:
#         print("NO")



# # L - ATM
# round(num,2)

# amount, acc_bal = [float(i) for i in input().split()]
# if amount%5 == 0 and amount < acc_bal:
#     print('%.2f' % (acc_bal - amount))
# elif amount%5 != 0 and amount < acc_bal:
#     print('%.2f' % acc_bal)
# else:
#     print('%.2f' % acc_bal)


# # M - Discount
#
# test_cases = int(input())
# s_price = 100
# for i in range(0,test_cases):
#     discount = int(input())
#     amount = (discount/100) * 100
#     print(int(s_price - amount))



# # N- Discount
#
# test_cases = int(input())
# for i in range(0,test_cases):
#     tv1_price, tv2_price, tv1_dis, tv2_dis = map(int, input().split())
#     tv1 = tv1_price - tv1_dis
#     tv2 = tv2_price - tv2_dis
#     if tv1 > tv2:
#         print("Second")
#     elif tv1 < tv2:
#         print("First")
#     else:
#         print("Any")
