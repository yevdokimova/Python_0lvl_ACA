user_input = [int(i) for i in input("Please enter the numbers: ").split()]

product = user_input[0] + user_input[1]

for i in range(1, len(user_input) - 1):
    current_product = user_input[i] * user_input[i + 1]
    if current_product > product:
        product = current_product

print(product)



