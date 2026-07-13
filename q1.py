roll_numbers = [101, 102, 105, 110, 115, 120]

roll = int(input("Enter roll number: "))

for i in range(len(roll_numbers)):
    if roll_numbers[i] == roll:
        print("Student found at position", i + 1)
        break
else:
    print("Student Not Found")
