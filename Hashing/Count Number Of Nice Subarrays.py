'''
Given an array of integers nums and an integer k. A continuous subarray is called nice if there are k odd numbers on it.

Return the number of nice sub-arrays.
'''

from collections import defaultdict

class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        # curr is number of odds in current subarray
        # ans is the number of suarrays we see that satisfy k
        curr = ans = 0
        # counts is the number of subarrays seen with the current number of odds
        counts = defaultdict(int)
        # number of subarrays with 0 odds is 1, the empty array []
        counts[0] = 1
        # for each subarray set ending at each number:
        for n in nums:
            # add 1 to the current number of odds if the new number is odd
            curr += n % 2 == 1
            # if we have seen a substring so far which would add the required number of odds
            # include this substring into it
            ans += counts[curr-k]
            # register we have seen a substring with this number of odds in the dict
            counts[curr] += 1
        return ans