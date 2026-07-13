n = int(input("Enter number of books: "))
book_ids = []

for i in range(n):
    book_ids.append(int(input("Enter Book ID: ")))

book_ids.sort()

book_id = int(input("Enter Book ID to search: "))

low = 0
high = len(book_ids) - 1

while low <= high:
    mid = (low + high) // 2

    if book_ids[mid] == book_id:
        print("Book found at position", mid + 1)
        break
    elif book_ids[mid] < book_id:
        low = mid + 1
    else:
        high = mid - 1
else:
    print("Book Not Found")