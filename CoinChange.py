class Solution:
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        max_number = amount + 1
        number_of_coins_per_amount = [max_number] * (amount+1)
        number_of_coins_per_amount[0] = 0
        value  = 1
        while value <= amount:
            for j in coins:
                if value >= j:
                    number_of_coins_per_amount[value] = min(number_of_coins_per_amount[value], number_of_coins_per_amount[value-j]+1)
            value+=1

        if number_of_coins_per_amount[amount] <= amount:
            return number_of_coins_per_amount[amount]
        else:
            return -1


solution = Solution()
# print(solution.coinChange([],10))
print(solution.coinChange([1],0))
#print(solution.coinChange([1, 2, 5],11))
# print(solution.coinChange([2],3))
#print(solution.coinChange([5,2,1],10))
# print(solution.coinChange([1,3,5],8))
# print(solution.coinChange([333,364,408,118,63,270,69,111,218,371,305],5615))

