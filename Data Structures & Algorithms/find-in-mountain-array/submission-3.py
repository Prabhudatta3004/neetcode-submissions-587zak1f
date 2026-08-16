class Solution:
    def findInMountainArray(self, target: int, mountainArr: 'MountainArray') -> int:
        ## finding the peak
        length = mountainArr.length()
        ## we need to check mid-1 , mid, mid+1
        start = 1 ## took from 1 cause we check mid-1
        end = length-2 ## took from length-2 because I use 1 indexed and mid+1

        while start<=end:
            mid = end + (start-end)//2

            prev, mide, nxt = mountainArr.get(mid-1), mountainArr.get(mid), mountainArr.get(mid+1)

            if prev<mide<nxt: ## in the left half so moving start to mid+1
                start = mid + 1
            elif prev>mide>nxt: ## in the right half so moving end to mid-1
                end = mid - 1
            else:
                break
            
        peak = mid

        ## checking for target in left half
        start  = 0
        end = peak-1
        while start<=end:
            mid = start +(end-start)//2

            if mountainArr.get(mid) > target:
                end = mid - 1
            elif mountainArr.get(mid) < target:
                start = mid + 1
            else:
                return mid
            
        ## checking for target in right half( descending order)
        start  = peak
        end = length-1
        while start<=end:
            mid = start +(end-start)//2

            if mountainArr.get(mid) <target:
                end = mid - 1
            elif mountainArr.get(mid) >target:
                start = mid + 1
            else:

                return mid
        return -1