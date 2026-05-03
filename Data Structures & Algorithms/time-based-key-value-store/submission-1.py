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
        seen = 0
        idx = -1
        while left <= right:
            mid = left+(right-left)//2
            if self.hashMap[key][mid][1] <= timestamp:
                if seen < self.hashMap[key][mid][1]:
                    seen = self.hashMap[key][mid][1]
                    idx = mid
                left = mid+1
            else:#if self.hashMap[key][mid][1] > timestamp:
                right = mid-1

        if seen == 0:
            return ""
        return self.hashMap[key][idx][0]

