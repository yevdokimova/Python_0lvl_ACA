numbers = list(map(int, input('Enter the numbers: ').split()))

products = []

for i in range(len(numbers) - 1):
    product = numbers[i] * numbers[i + 1]
    products.append(product)

print(max(products))

