# 100 days given, print how many years, months, days

days = int(input("Enter days:"))

if days>=365:
    years = days//365
    print(years, "years", end=", ")
    left_days = days - (years*365)
    months = left_days//30
    print(months, "months" , end=", ")
    left_days_day = left_days - (months*30)
    print(left_days_day, "days")
else:
    print("0 years" , end=", ")
    months = days // 30
    print(months, "months" , end=", ")
    left_days_day = days - (months*30)
    print(left_days_day, "days")

