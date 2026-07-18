class Solution:
    def findGCD(self, nums: List[int]) -> int:
        nums = sorted(nums)
        n = len(nums)
        if nums[n-1] // nums[0] == nums[0]:
            return nums[0]
        a = nums[0]
        b= nums[n-1]
        while(b!=0):
            a,b=b,a%b
        return a
        
