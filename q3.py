n = int(input("Enter number of students: "))
marks = []
for i in range(n):
    marks.append(int(input("Enter marks: ")))
marks.sort()
print("Marks in ascending order:", marks)
