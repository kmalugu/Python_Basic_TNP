# 100 days given, print how many years, months, days

days = int(input("Enter days:"))

if days>=365:
    years = days//365
    print(years, "years")
    left_days = days - 365
    months = left_days//30
    print(months, "months")
    left_days_day = left_days - 30
    print(left_days_day, "days")
else:
    print("0 years")
    months = days // 30
    print(months, "months")
    left_days_day = days - (months*30)
    print(left_days_day, "days")

