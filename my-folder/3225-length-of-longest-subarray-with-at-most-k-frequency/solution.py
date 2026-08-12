class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        left  = 0
        count = {}
        l = 0
        for right, ele in enumerate(nums):
            count[ele] = count.get(ele, 0) + 1
            while count[ele] > k:
                count[nums[left]] -= 1
                left += 1
            l = max(l, right-left+1)
        return l


            

        
