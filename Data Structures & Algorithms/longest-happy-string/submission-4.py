class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        maxheap=[]
        if a>0:
            heapq.heappush(maxheap,(-a,"a"))
        if b>0:
            heapq.heappush(maxheap,(-b,"b"))
        if c>0:
            heapq.heappush(maxheap,(-c,"c"))
    
        res = []
        while maxheap:
            freq1,ch1 = heapq.heappop(maxheap)
            if len(res)>=2 and res[-2] == res[-1] == ch1:
                if not maxheap:
                    break
                freq2,ch2 = heapq.heappop(maxheap)
                res.append(ch2)
                freq2+=1
                if freq2<0:
                    heapq.heappush(maxheap,(freq2,ch2))
                heapq.heappush(maxheap,(freq1,ch1))
            else:
                freq1+=1
                res.append(ch1)
                if freq1<0:
                    heapq.heappush(maxheap,(freq1,ch1))
        return ''.join(res)            