n = int(input("Enter number of patients: "))
patients = []

for i in range(n):
    priority = int(input("Enter priority for Patient" + str(i + 1) + ": "))
    patients.append(["Patient" + str(i + 1), priority])

patients.sort(reverse=True)

print("Emergency Queue:")

for patient in patients:
    print(patient[0])