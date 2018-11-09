def solution(X, Y, D):
    intermediateResult = ((Y-X)//D)
    if (Y-X)%D == 0:
        return intermediateResult
    else:
        return intermediateResult+1

print(solution(10,99,30))