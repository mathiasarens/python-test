def fibRec(n):
    if n <= 0:
        return 0
    if n == 1:
        return 1
    if n == 2:
        return 2
    return fibRec(n-1)+fibRec(n-2)

def fibIt(n):
    if n <= 0:
        return 0
    fib = [0] * (max(2,n)+1)
    fib[1]=1
    fib[2]=2
    for i in range(3,n+1):
        fib[i] = fib[i-1]+fib[i-2]
    return fib[n]

print(fibRec(-1) == 0)
print(fibRec(0) == 0)
print(fibRec(1) == 1)
print(fibRec(2) == 2)
print(fibRec(3) == 3)
print(fibRec(4) == 5)
print(fibRec(5) == 8)
print(fibRec(6) == 13)
print(fibRec(7) == 21)

print(fibIt(-1) == 0)
print(fibIt(0) == 0)
print(fibIt(1) == 1)
print(fibIt(2) == 2)
print(fibIt(3) == 3)
print(fibIt(4) == 5)
print(fibIt(5) == 8)
print(fibIt(6) == 13)
print(fibIt(7) == 21)