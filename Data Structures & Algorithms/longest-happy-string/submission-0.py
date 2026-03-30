class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        maxheap = []
        res = []
        if a>0:
            heapq.heappush(maxheap,(-a,"a"))
        if b>0:
            heapq.heappush(maxheap,(-b,"b"))
        if c>0:
            heapq.heappush(maxheap,(-c,"c"))

        while maxheap:
            count1,value = heapq.heappop(maxheap)

            if len(res)>=2 and res[-1] == res[-2] == value:
                if not maxheap:
                    break
                
                count2,value2 = heapq.heappop(maxheap)
                res.append(value2)
                count2 +=1

                if count2<0:
                    heapq.heappush(maxheap,(count2,value2))
                
                heapq.heappush(maxheap,(count1,value))
            else:
                count1 +=1
                res.append(value)
                if count1 < 0:
                    heapq.heappush(maxheap,(count1,value))
        
        return "".join(res)
                
