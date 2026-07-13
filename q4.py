n = int(input("Enter number of participants: "))
timings = []

for i in range(n):
    timings.append(float(input("Enter timing in seconds: ")))

timings.sort()

print("Timings from fastest to slowest:", timings)