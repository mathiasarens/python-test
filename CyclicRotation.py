def solution(A, K):
    if len(A) == 0:
        return A
    else:
        rotationAfterModulo = K % len(A)
        if rotationAfterModulo > 0:
            return A[-rotationAfterModulo:]+A[:-rotationAfterModulo]
        else:
            return A

array = []
print(array)
print(solution(array, 12))