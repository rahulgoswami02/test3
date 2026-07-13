roll_numbers = [101, 102, 105, 110, 115, 120]

search = int(input("Search roll number: "))

for i in range(len(roll_numbers)):
    if roll_numbers[i] == search:
        print("Student found at position", i + 1)
        break
else:
    print("Student Not Found")
