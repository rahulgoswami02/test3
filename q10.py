class School:
    def annual_report(self):
        n = int(input("Enter number of students: "))
        marks = []

        for i in range(n):
            marks.append(int(input("Enter marks for Student" + str(i + 1) + ": ")))

        marks.sort()

        print("Marks in ascending order:", marks)

        mark = int(input("Enter mark to search: "))

        low = 0
        high = len(marks) - 1

        while low <= high:
            mid = (low + high) // 2

            if marks[mid] == mark:
                print("Mark found at position", mid + 1)
                break
            elif marks[mid] < mark:
                low = mid + 1
            else:
                high = mid - 1
        else:
            print("Mark Not Found")

s = School()
s.annual_report()