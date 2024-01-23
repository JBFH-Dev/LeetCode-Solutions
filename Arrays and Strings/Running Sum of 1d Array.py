# Given an array nums. We define a running sum of an array as runningSum[i] = sum(nums[0]…nums[i]). 
# Return the running sum of nums.

class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        priority = [nums[0]]
        
        for i in nums[1:]:
            priority.append(priority[-1] + i)
        return priority