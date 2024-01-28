'''
Given a 2D integer array nums where nums[i] is a non-empty array of distinct positive integers, return the list of integers that are present in each array of nums sorted in ascending order.
 
'''

from collections import defaultdict

class Solution:
    def intersection(self, nums: List[List[int]]) -> List[int]:
        # Slower
        '''
        counter = defaultdict(dict[int])
        out = []
        allLists = set(range(len(nums)))
        for i, l in enumerate(nums):
            for n in l:
                if n in counter:
                    counter[n][i] = 1
                else:
                    counter[n] = {i: 1}
                if counter[n].keys() == allLists:
                        out.append(n)
        return sorted(out)
        '''

        # Faster
        if len(nums) == 1:
            nums[0].sort()
            return nums[0]

        targets = set(nums[0])
        for i in nums[1::]:
            targets &= set(i)
        
        targets = list(targets)
        targets.sort()
        return targets