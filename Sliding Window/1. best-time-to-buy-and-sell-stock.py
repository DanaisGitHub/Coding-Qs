class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        currSmallest = prices[0]
        currLargest = -1
        bestDiff = -1
        for i in range(len(prices)):
            if prices[i]<currSmallest:
                currSmallest = prices[i]
                currLargest = -1
                continue
            if prices[i]> currLargest:
                currLargest = prices[i]
                currDiff = currLargest - currSmallest
                if currDiff > bestDiff:
                    bestDiff = currDiff
                    
        maxProfit = currLargest - currSmallest
        if bestDiff <=0:
            return 0
        return bestDiff
        
        
print(Solution.maxProfit("",[2,4,1]))



class SolutionBetter:
    def maxProfit(self, prices: List[int]) -> int:
        bestDiff = 0
        
        lowest = prices[0]
        for price in prices:
            if price < lowest:
                lowest = price
            bestDiff = max(bestDiff, price - lowest)
        return bestDiff