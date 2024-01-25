'''
Given a string s and an integer k, return the maximum number of vowel letters in any substring of s with length k.

Vowel letters in English are 'a', 'e', 'i', 'o', and 'u'.
'''

class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        curr = 0
        most = 0
        vowels = 'aeiou'
        start = 0
        l = 0
        for end in range(len(s)):
            l += 1
            if s[end] in vowels:
                curr += 1
            while l > k and start <= end:
                if s[start] in vowels:
                    curr -= 1
                l -= 1
                start += 1
            if curr == k:
                return k
            if curr > most:
                most = curr
        return most