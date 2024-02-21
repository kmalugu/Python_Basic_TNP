#Check if the number is even AND Prime
val = int(input("Enter No. : "))
count = 0
for i in range(1,(val)+1):
    if val % i == 0:
        count += 1
if (val % 2 == 0) and (count == 2):
    print(True)
else:
    print(False)


# Is it raining OR snowing (True if either is true)
rain = input("Enter Yes or No:")
snow = input("Enter Yes or No:")
l_rain = rain.lower()
l_snow = snow.lower()
if l_rain == "yes" or l_snow == "yes":
    print(True)
else:
    print(False)



#


