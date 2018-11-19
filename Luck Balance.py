def luckBalance(k, contests):
    contests.sort(key=lambda x: (-x[1], -x[0]))
    luck = 0
    for i in range(len(contests)):
        if (i <= k and contests[i][1]==1) or contests[i][1]==0:
            luck+=contests[i][0]
        elif i > k and contests[i][1] == 1:
            luck-=contests[i][0]
        else:
            print("Should not happen - ERROR")
    return luck

print(luckBalance() == 29)