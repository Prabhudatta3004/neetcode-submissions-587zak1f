class CountSquares:

    def __init__(self):
        self.hashmap = defaultdict(int)
        self.point_list = []
    def add(self, point: List[int]) -> None:
        self.hashmap[tuple(point)] +=1
        self.point_list.append(point)

    def count(self, point: List[int]) -> int:
        res = 0
        x1,y1 = point

        for x,y in self.point_list:
            if (abs(y-y1) != abs(x-x1)) or x == x1 or y == y1:
                continue
            
            res += self.hashmap[(x,y1)] * self.hashmap[(x1,y)]
        return res
