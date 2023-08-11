"""
#blind75
Leetcode 121
say you have an array for which the ith  element is the price of a given stock on day i
If you were only permitted to complete at most one transaction(ie buy one and ell one share of stock)
design an algorithm to find maximum profit
Note you cannot sell a stock befor you buy one

Example:
[7,1,5,3,6,4]

output =5

Explanation: buy on day 2 (price =1) sell on day 5(price =6) profit 6-1 =5
not 7-1 =6 because selling price needs to be higher than buying price
"""

def max_profit(prices:list[int]):
    l,r =0,1
    maxP =0
    while r < len(prices):
        if prices[l] < prices[r]:
            profit = prices[r] - prices[l]
            maxP =max(maxP,profit)

        else:
            l=r
        r +=1   

    return maxP

print(max_profit([7,1,5,3,6,4]))