'''
You are given two strings s and t of the same length and an integer maxCost.

You want to change s to t. Changing the ith character of s to ith character of t costs |s[i] - t[i]| (i.e., the absolute difference between the ASCII values of the characters).

Return the maximum length of a substring of s that can be changed to be the same as the corresponding substring of t with a cost less than or equal to maxCost. If there is no substring from s that can be changed to its corresponding substring from t, return 0.
'''

class Solution:
    def changeCost(self, a: str, b: str) -> int:
        return abs(ord(a) - ord(b))

    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        maxLen = 0
        start = 0
        currLen = 0
        currCost = 0
        for end in range(len(s)):
            currLen += 1
            currCost += self.changeCost(s[end], t[end])
            while currCost > maxCost and start <= end:
                currCost -= self.changeCost(s[start], t[start])
                currLen -= 1
                start += 1
            if currLen > maxLen:
                maxLen = currLen
        return maxLen

    