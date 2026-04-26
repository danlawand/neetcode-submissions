class Solution:
    # Time Complexity O(n.log n) 
    # Auxiliary memory O(2*n)
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        n = len(position)
        carsTuple = []
        # N
        for i in range(n):
            carsTuple.append((position[i], speed[i]))

        # O(n.log n)
        carsTuple.sort(reverse=True)

        # O(n)
        stack = []
        for p, s in carsTuple:
            timeToTarget = (target-p)/s
            stack.append(timeToTarget)
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()

        return len(stack)
