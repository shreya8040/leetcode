class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        s = sum(nums)
        n = len(nums)
        lsum = 0
        flag = 0
        for i in range(0,n):
            rsum = s - lsum
            lsum = lsum + nums[i]
            if lsum == rsum:
                flag = flag + 1
                return i
            
        if flag == 0:
            return -1
            
