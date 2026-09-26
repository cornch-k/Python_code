a = int(input())
nameboard = ["PROBRAIN", "GROW", "ARGOS", "ADMIN", "ANT", "MOTION", "SPG", "COMON", "ALMIGHTY"]
maxscoreboard = []

for i in range(9):
    scoresum = []
    scoresum = list(map(int, input().split()))
    maxscoreboard.append(max(scoresum))
print(nameboard[maxscoreboard.index(max(maxscoreboard))])