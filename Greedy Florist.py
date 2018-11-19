
def getMinimumCost(k, c):
    min_costs = 0
    if k < len(c):
        c.sort()
        c.reverse()
        k_times = 1
        k_counter = 1
        for cost in c:
            min_costs+=k_times*cost
            if k_counter < k:
                k_counter+=1
            else:
                k_counter=1
                k_times+=1
    else:
        min_costs = sum(c)
    return min_costs

print(getMinimumCost(3, [2,5,6]) == 13)
print(getMinimumCost(2, [2,5,6]) == 15)
print(getMinimumCost(3, [1,3,5,7,9]) == 29)
# Invalid: 3610289864
# Correct: 163578911
print(getMinimumCost(3, [390225,426456,688267,800389,990107,439248,240638,15991,874479,568754,729927,980985,132244,488186,5037,721765,251885,28458,23710,281490,30935,897665,768945,337228,533277,959855,927447,941485,24242,684459,312855,716170,512600,608266,779912,950103,211756,665028,642996,262173,789020,932421,390745,433434,350262,463568,668809,305781,815771,550800]) == 163578911)