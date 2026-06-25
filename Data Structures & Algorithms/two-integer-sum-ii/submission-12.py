class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        start =0
        end = len(numbers)-1

        while start < end:

            sum_up = numbers[start] + numbers[end]

            if sum_up > target:
                end -=1
            elif sum_up < target:
                start +=1
            else:
                return [start+1,end+1]