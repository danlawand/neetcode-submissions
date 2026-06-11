class Solution:
    # Time O(2^n)
    # Space O(1) or 2^n?
    def _recClimbStairs(self, n: int) -> int:
        if n <= 0:
            return 0
        if n == 1 or n == 2:
            return n

        return self.climbStairs(n-1) + self.climbStairs(n-2)
    
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n

        self.mem = [0]*(n+1)
        self.mem[1] = 1
        self.mem[2] = 2
        for i in range(3, n+1):
            self.mem[i] = self.mem[i-1]+self.mem[i-2]
        return self.mem[n]

