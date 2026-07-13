n = int(input("Enter number of products: "))
ids = []

for i in range(n):
    product_id = int(input("Enter Product ID: "))
    ids.append(product_id)

ids.sort()

print("Product IDs in ascending order:", ids)

target = int(input("Enter Product ID to search: "))

low = 0
high = n - 1

while low <= high:
    mid = (low + high) // 2

    if ids[mid] == target:
        print("Product Found at index", mid)
        break
    elif ids[mid] < target:
        low = mid + 1
    else:
        high = mid - 1
else:
    print("Product Not Available")