class TimeMap:

    def __init__(self):
        self.data = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.data:
            self.data[key].append((value, timestamp))
        else:
            self.data[key] = [(value, timestamp)]

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.data:
            return ""
        l, r = 0, len(self.data[key])-1
        while l<r:
            mid = math.ceil(float(l+r)/2)
            if self.data[key][mid][1] == timestamp:
                return self.data[key][mid][0]
            elif self.data[key][mid][1] > timestamp:
                r = mid-1
            else:
                l = mid
        if self.data[key][r][1] <= timestamp:
            return self.data[key][r][0]
        if self.data[key][l][1] <= timestamp:
            return self.data[key][l][0]
        return ""
