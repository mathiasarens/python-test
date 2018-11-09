def solution(N):
    print(bin(N)[2:])
    maxBinaryGap = 0
    currentBinaryGap = -1
    binaryRepresentation = bin(N)[2:]
    for i, c in enumerate(binaryRepresentation):
       if currentBinaryGap >= 0:
           if c == '0':
            currentBinaryGap+=1
           else:
            if currentBinaryGap > maxBinaryGap:
                maxBinaryGap = currentBinaryGap
            currentBinaryGap = 0
       else:
           if c == '1':
               currentBinaryGap=0

    return maxBinaryGap

print(solution(32))