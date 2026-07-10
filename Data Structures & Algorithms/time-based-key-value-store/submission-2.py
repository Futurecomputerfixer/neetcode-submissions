class TimeMap:

    def __init__(self):
        self.store = defaultdict(dict)

    def set(self, key: str, value: str, timestamp: int) -> None:
        (self.store[key])[timestamp] = value

    def get(self, key: str, timestamp: int) -> str:
        D = self.store[key]
        if not D: return ""

        times = sorted(D.keys())
        res = ""

        l, r = 0, len(times) - 1
        while l <= r:
            m = (l+r) //2
            if times[m] > timestamp:
                r = m - 1
            else:
                res = D[times[m]]
                l = m+1
        
        return res

        
