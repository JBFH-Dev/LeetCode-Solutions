'''
Given an array of integers nums, calculate the pivot index of this array.

The pivot index is the index where the sum of all the numbers strictly to the left of the index is equal to the sum of all the numbers strictly to the index's right.

If the index is on the left edge of the array, then the left sum is 0 because there are no elements to the left. This also applies to the right edge of the array.

Return the leftmost pivot index. If no such index exists, return -1.

'''

class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        a = 0
        prefix = []
        for i in nums:
            prefix.append(a+i)
            a += i

        prefix.insert(0, 0)
        prefix.append(prefix[-1])

        pivots = []
        for i in range(len(nums)):
            leftSum = prefix[i]
            rightSum = prefix[-1] - prefix[i+1]
            if rightSum == leftSum:
                return i
        return -1