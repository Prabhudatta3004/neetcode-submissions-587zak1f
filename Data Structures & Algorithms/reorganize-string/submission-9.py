class Solution:
    def reorganizeString(self, s: str) -> str:
        freq = Counter(s)

        max_freq = max(freq.values())

        if max_freq > (len(s)+1)//2:
            return ""
        maxheap = []
        for ch,freq in freq.items():
            heapq.heappush(maxheap,(-freq,ch))
        res= []
        while maxheap:
            freq1,ch1 = heapq.heappop(maxheap)
            if res and res[-1] == ch1:
                if not maxheap:
                    return ""
                
                freq2,ch2 = heapq.heappop(maxheap)
                res.append(ch2)
                freq2+=1
                if freq2<0:
                    heapq.heappush(maxheap,(freq2,ch2))
                heapq.heappush(maxheap,(freq1,ch1))
            else:
                res.append(ch1)
                freq1 +=1
                if freq1<0:
                    heapq.heappush(maxheap,(freq1,ch1))
        return "".join(res)
