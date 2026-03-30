from collections import Counter
class Solution:
    def reorganizeString(self, s: str) -> str:
        st_freq = Counter(s)

        max_freq = max(st_freq.values())
        if max_freq > (len(s)+1)//2:
            return ""

        ## we use a maxheap to get max freq

        maxheap = []
        for char, freq in st_freq.items():
            heapq.heappush(maxheap, (-freq, char))
        res= []
        while maxheap:
            count1,char = heapq.heappop(maxheap)

            if res and res[-1] == char:
                if not maxheap:
                    return ""
                
                count2,char2 = heapq.heappop(maxheap)
                res.append(char2)
                count2 +=1
                if count2<0:
                    heapq.heappush(maxheap,(count2,char2))
                heapq.heappush(maxheap,(count1,char))
            else:
                res.append(char)
                count1 +=1
                if count1<0:
                    heapq.heappush(maxheap,(count1,char))
        return "".join(res)

        