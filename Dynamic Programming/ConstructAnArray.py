def countArray(n, k, x):
    # Return the number of ways to fill in the array.

    result = ((k-1)**(n-1))%1000000007
    if x == 1:
        return result -1
    else:
        return result


print(countArray(4, 3, 2) == 3)
print(countArray(5, 3, 2) == 5)
print(countArray(4, 4, 2) == 7)
print(countArray(5, 4, 4) == 20)
print(countArray(761,99,1) == 236568308)
print(countArray(761,99,1))



# 1 2 1 2 4
# 1 2 1 3 4
# 1 2 3 1 4
# 1 2 3 2 4
# 1 2 4 1 4
# 1 2 4 2 4
# 1 2 4 3 4
# 1 3 1 2 4
# 1 3 1 3 4
# 1 3 2 1 4
# 1 3 2 3 4
# 1 3 4 1 4
# 1 3 4 1 4
# 1 3 4 3 4
# 1 4 1 2 4
# 1 4 1 3 4
# 1 4 2 1 4
# 1 4 2 3 4
# 1 4 3 1 4
# 1 4 3 2 4

# 1 2 1 2
# 1 2 3 2
# 1 2 4 2
# 1 3 1 2
# 1 3 4 2
# 1 4 1 2
# 1 4 3 2

# 1 2 1 3 2
# 1 2 3 1 2
# 1 3 1 3 2
# 1 3 2 3 2
# 1 3 2 1 2

# 1 2 1 2
# 1 2 3
# 1 3 1
# 1 3 2
