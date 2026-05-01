class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = max(piles)
        res = right
        while left <= right:
            mid = (right+left)//2
            totalTime = 0
            for pile in piles:
                totalTime += math.ceil(pile/mid)

            if totalTime <= h:
                res = mid
                right = mid-1
            else:
                left = mid+1
        return res



    def _minEatingSpeed(self, piles: List[int], h: int) -> int:
        n = len(piles)
        if n > h:
            return -1

        currK = 0
        maxBananas = max(piles)
        for k in range(1,maxBananas+1):
            leftHours = h
            for bananas in piles:
                leftHours -= math.ceil(bananas/k)
                if leftHours < 0:
                    break
            if leftHours >= 0:
                return k
        return -1