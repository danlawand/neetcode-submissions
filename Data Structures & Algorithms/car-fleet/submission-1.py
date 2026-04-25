class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        n = len(position)
        cars = []
        for i in range(n):
            cars.append((position[i], speed[i]))
        
        cars.sort(reverse=True)

        stack = []
        for p, s in cars:
            timeConsumed = (target - p)/s
            stack.append(timeConsumed)
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()
        return len(stack)