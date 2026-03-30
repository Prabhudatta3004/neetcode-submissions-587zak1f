class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        start = 0
        end = len(numbers)-1

        while start<end:
            su = numbers[start]+numbers[end]
            if su == target:
                return [start+1,end+1]
            
            if su> target:
                end -=1
            else:
                start +=1
        
        