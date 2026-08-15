class TimeMap:

    def __init__(self):
        self.kv_store = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.kv_store:
            self.kv_store[key].append((value,timestamp))
        else:
            self.kv_store[key] = [(value,timestamp)]

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.kv_store:
            return ""
        values_list = self.kv_store[key]

        start = 0
        end = len(values_list)-1
        candidate = ''
        while start <= end:
            mid = start + (end-start)//2

            if values_list[mid][1] == timestamp:
                return values_list[mid][0]
            
            if values_list[mid][1] < timestamp:
                candidate = values_list[mid][0]
                start = mid+1
            else:
                end = mid-1
        return candidate

