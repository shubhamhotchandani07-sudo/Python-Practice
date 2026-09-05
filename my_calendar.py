import calendar

year = int(input("Enter a Year: "))
month = int(input("Enter a Month: "))

cal = calendar.month(year, month)
print(cal)
