def digit_sum(num):
    if num == 0:
        return 0
    return num % 10 + digit_sum(num // 10)


number = int(input('Enter a  number: '))
print(digit_sum(number))

# example for 123
# 3 + digit_sum(12) ## 3 + 2 + digit_sum(1) ###3 + 2 + 1 + digit_sum(0)

