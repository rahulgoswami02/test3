class Race:
    def rank_participants(self):
        n = int(input("Enter number of participants: "))
        timings = []

        for i in range(n):
            timings.append(float(input("Enter timing in seconds: ")))

        timings.sort()
        print("Timings from fastest to slowest:", timings)

r = Race()
r.rank_participants()