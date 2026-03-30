class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        def backtrack(curr_start,path):
            res.append(path[:])

            for choice in range(curr_start,len(nums)):
                if choice>curr_start and nums[choice]==nums[choice-1]:
                    continue
                path.append(nums[choice])
                backtrack(choice+1,path)
                path.pop()
        
        backtrack(0,[])
        return res