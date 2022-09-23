year = int(input('Please enter the year which you want to convert: '))

if year  >= 1 and year <= 2021:
    century = year // 100
    if year % 100 != 0:
        century = century + 1

print(century)