year = input("Введите год: ")
year = int(year)
is_leap = year % 4 ==0 and (year % 100 != 0 or year % 400 ==0)
print(is_leap)2000