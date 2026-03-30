class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        start = 0
        end = len(numbers)-1

        while start < end:
            twosum = numbers[start]+numbers[end]
            if twosum>target:
                end -=1
            elif twosum < target:
                start +=1
            else:
                return [start+1,end+1]
