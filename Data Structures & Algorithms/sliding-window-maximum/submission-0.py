class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        start = end = 0
        q = deque() ## to store the indices
        res = []

        while end < len(nums):
            ## adding the end index to the queue only if
            ## the end value is larger than the last
            ## stored values and keep on removing
            ## the smaller valued indices since they are useless

            while q and nums[q[-1]] < nums[end]:
                q.pop()
            
            ## Now add the current index to the queue
            q.append(end)


            if end-start+1 < k:
                end +=1 
            elif end-start+1 == k:
                res.append(nums[q[0]])
                ## now popping out older max values

                if start == q[0]:
                    q.popleft()
                start +=1
                end +=1
        return res