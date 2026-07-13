n1 = int(input("Enter number of employees in branch 1: "))
salary1 = []

for i in range(n1):
    salary1.append(int(input("Enter salary in thousands: ")))

n2 = int(input("Enter number of employees in branch 2: "))
salary2 = []

for i in range(n2):
    salary2.append(int(input("Enter salary in thousands: ")))

salaries = salary1 + salary2
salaries.sort()

print("Salaries in ascending order:", salaries)