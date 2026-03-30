class TimeMap:

    def __init__(self):
        ##Lets declare a KVS
        self.store ={} ## KEY: value ([value,timestamp])

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.store:
            self.store[key] = []
        self.store[key].append([value,timestamp])

    def get(self, key: str, timestamp: int) -> str:
        res = ""
        start = 0
        value = self.store.get(key, [])
        end = len(value)-1

        while start<=end:
            mid = start + (end-start)//2

            if value[mid][1] <= timestamp:
                res = value[mid][0]
                start = mid + 1
            else :
                end = mid - 1

        return res