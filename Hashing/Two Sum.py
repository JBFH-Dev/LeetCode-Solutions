'''
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.
'''

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numsDict = {}
        for i, n in enumerate(nums):
            if n in numsDict:
                numsDict[n].append(i)
            else:
                numsDict[n] = [i]
        for i, n in enumerate(nums):
            targ = target - n
            if targ == n:
                if targ in numsDict and len(numsDict[targ]) >= 2:
                    return [i, numsDict[targ][1]]
            elif targ in numsDict:
                return [i, numsDict[targ][0]]