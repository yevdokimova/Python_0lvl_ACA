# Write a program that allows user to transform year to century multiple time.

hint = 'Please input e year(YYYY) or Q to exit: '

year = input(hint)

while year != 'Q':
    year = int(year)

    while year < 1 or year > 2021:
        print('Year is wrong. Please input a year between 1 and 2021')
        year = int(input('Please enter a year(YYYY): '))

    century = year // 100

    if year % 100 != 0:
        century += 1

    print(century)
    year = input(hint)
