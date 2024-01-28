'''
Given a string s, return true if s is a good string, or false otherwise.

A string s is good if all the characters that appear in s have the same number of occurrences (i.e., the same frequency).
'''

from collections import defaultdict

class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        # attempt 1
        counter = defaultdict(int)
        for l in s:
            if l in counter:
                counter[l] += 1
            else:
                counter[l] = 1
        return len(set(counter.values())) == 1
            