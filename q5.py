n = int(input("Enter number of books: "))
prices = []

for i in range(n):
    prices.append(float(input("Enter book price: ")))

prices.sort()

new_price = float(input("Enter new book price: "))

prices.append(new_price)
prices.sort()

print("Book prices after insertion:", prices)