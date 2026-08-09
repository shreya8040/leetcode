class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        sumr = nums[0]
        msum = []
        for i in range(1,len(nums)):
            if nums[i-1]>=nums[i]:
                msum.append(sumr)
                sumr = nums[i]
            else:
                sumr = sumr+ nums[i]

        return max(max(msum, default = sumr),sumr)
        
