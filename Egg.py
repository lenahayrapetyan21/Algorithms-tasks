
floors = int(input())
eggs = int(input())
drops = 0
dp = [0] * (eggs + 1)
while dp[eggs] < floors:
    drops += 1
    for i in range(eggs, 0, -1):
        broken = dp[i - 1]
        not_broken = dp[i]
        dp[i] = broken + not_broken + 1

print(drops)
