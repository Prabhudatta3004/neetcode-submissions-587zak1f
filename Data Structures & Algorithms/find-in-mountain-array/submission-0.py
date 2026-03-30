class Solution:
    def findInMountainArray(self, target: int, mountainArr: 'MountainArray') -> int:
        length = mountainArr.length()

        ## finding the peak

        left,right = 1, length-2

        while left<=right:
            mid = left + (right-left)//2

            prev,mide,nxt = mountainArr.get(mid-1),mountainArr.get(mid),mountainArr.get(mid+1)

            if prev<mide<nxt:
                left = mid+1
            elif prev>mide>nxt:
                right = mid-1
            else:
                break

        peak = mid
        

        ## search in left sorted part
        left,right = 0, peak-1

        while left<=right:
            mid = left + (right-left)//2

            mid_ele = mountainArr.get(mid)

            if mid_ele < target:
                left = mid + 1
            elif mid_ele > target:
                right = mid - 1
            else:
                return mid
        
        left,right =peak,length-1

        ## search in right sorted part
        while left<=right:
            mid = left + (right-left)//2

            mid_ele = mountainArr.get(mid)

            if mid_ele > target:
                left = mid + 1
            elif mid_ele < target:
                right = mid - 1
            else:
                return mid
        return -1
        