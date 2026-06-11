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
        self.mem = [-1]*(n+1)
        return self.recursiveClimbStairs(n)

    def recursiveClimbStairs(self, n: int) -> int:
        if n <= 0:
            return 0
        if n == 1 or n == 2:
            self.mem[n] = n
        if self.mem[n] != -1:
            return self.mem[n]
        
        self.mem[n] = self.recursiveClimbStairs(n-1) + self.recursiveClimbStairs(n-2)
        return self.mem[n]
