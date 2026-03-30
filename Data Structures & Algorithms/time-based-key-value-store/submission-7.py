class TimeMap:

    def __init__(self):
        self.map = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.map:
            self.map[key] = []
        self.map[key].append((value,timestamp))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.map:
            return ""
        
        values = self.map.get(key,[])

        start = 0
        end = len(values)-1
        res = ''
        while start <= end:
            mid = start + (end-start)//2

            if values[mid][1] == timestamp:
                return values[mid][0]
            elif values[mid][1] < timestamp:
                res = values[mid][0]
                start = mid + 1
            else:
                end = mid - 1
        return res