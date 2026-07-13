n = int(input("Enter number of players: "))
scores = []

for i in range(n):
    scores.append(int(input("Enter score: ")))

scores.sort(reverse=True)

print("Leaderboard scores:", scores)