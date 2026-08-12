class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        n = len(nums)
        subs = []

        for i in range(n - 2):
            if nums[i] > 0:
                break 
            if i > 0 and nums[i] == nums[i - 1]:
                continue 
            if nums[i] + nums[i + 1] + nums[i + 2] > 0:
                break  
            if nums[i] + nums[n - 2] + nums[n - 1] < 0:
                continue  
            left, right = i + 1, n - 1
            target = -nums[i]
            while left < right:
                s = nums[left] + nums[right]
                if s < target:
                    left += 1
                elif s > target:
                    right -= 1
                else:
                    subs.append([nums[i], nums[left], nums[right]])
                    left += 1
                    right -= 1
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1

        return subs


        
