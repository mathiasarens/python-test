import bisect
# Complete the triplets function below.
def triplets(a, b, c):
    a_sorted = sorted(set(a))
    b_set = set(b)
    c_sorted = sorted(set(c))
    num_triplets = 0
    for value in b_set:
        index_lower = bisect.bisect_right(a_sorted, value)
        index_higher = bisect.bisect_right(c_sorted, value)
        if index_lower > 0 and index_higher > 0:
            num_triplets += index_lower * index_higher
    return num_triplets

print(triplets([1],[1],[1]) == 1)
print(triplets([1,2],[1,2],[1,3]) == 3)
print(triplets([1,1],[1],[1]) == 1)
print(triplets([1,1],[1,2,1],[1]) == 2)
print(triplets([1,3,5],[2,3],[1,2,3]) == 8)
print(triplets([1,4,5],[2,3,3],[1,2,3]) == 5)
print(triplets([1,3,5,7],[5,7,9],[7,9,11,13]) == 12)
print(triplets([1,2,3],[1,2,3],[1,2,3]) == 14)

