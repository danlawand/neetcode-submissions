class TimeMap:

    def __init__(self):
        self.hashMap = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.hashMap:
            self.hashMap[key].append((value, timestamp))
        else:
            self.hashMap[key] = [(value, timestamp)]
    # 1 3 4 5 6
    # ^ ^
    # t 2

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.hashMap:
            return ""
        n = len(self.hashMap[key])
        left = 0
        right = n-1
        while left <= right:
            mid = left+(right-left)//2
            if self.hashMap[key][mid][1] == timestamp:
                return self.hashMap[key][mid][0]
            elif self.hashMap[key][mid][1] > timestamp:
                right = mid-1
            else:
                left = mid+1
        print(left)
        if left >= 0 and left < n:
            if self.hashMap[key][left][1] <= timestamp:
                return self.hashMap[key][left][0]
        if left > 0 and self.hashMap[key][left-1][1] <= timestamp:
            return self.hashMap[key][left-1][0]
        return ""

