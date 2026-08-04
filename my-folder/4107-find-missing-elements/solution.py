class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        nums = sorted(nums)
        n = len(nums)
        ar =[]
        for i in range(0,n):
            if i-1<0:continue
            if nums[i]-nums[i-1]>1:
                for j in range(nums[i-1],nums[i]-1):
                    ar.append(j+1)
        return ar



