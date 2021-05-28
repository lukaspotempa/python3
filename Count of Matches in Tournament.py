n = 14
gamesPlayed = 0
while n > 1:
    if (n % 2) > 0:
        n -= 1
        gamesPlayed += 1
    gamesPlayed += n/2
    n /= 2
print(int(gamesPlayed))


