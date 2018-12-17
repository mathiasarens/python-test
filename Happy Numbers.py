def numSquareNum(n):
    sum = 0
    while n > 0:
        sum += (n % 10) ** 2
        n //= 10
    return sum

def happyNumber(n):
    slow = n
    fast = n
    while True:
        slow = numSquareNum(slow)
        fast = numSquareNum(numSquareNum(fast))
        if slow != fast:
            continue
        else:
            break
    return slow == 1

print(numSquareNum(19))
print(happyNumber(19))
print(happyNumber(20))