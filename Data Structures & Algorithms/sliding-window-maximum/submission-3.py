class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q = deque()
        start = end = 0
        res = list()

        while end < len(nums):
            while q and nums[q[-1]] < nums[end]:
                q.pop()
            
            q.append(end)
            end +=1

            if end-start == k:
                res.append(nums[q[0]])

                if start == q[0]:
                    q.popleft()
                start +=1
        return res