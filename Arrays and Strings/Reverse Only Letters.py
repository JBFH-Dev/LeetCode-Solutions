'''
Given a string s, reverse the string according to the following rules:

All the characters that are not English letters remain in the same position.
All the English letters (lowercase or uppercase) should be reversed.
Return s after reversing it.

'''

class Solution:
    def reverseOnlyLetters(self, s: str) -> str:

        scanner = len(s)
        out = [i for i in s]
        printer = 0

        for scanner in range(len(s)-1, -1, -1):
            if s[scanner].isalpha():
                while not out[printer].isalpha() and printer < len(s):
                    printer += 1
                out[printer] = s[scanner]
                printer += 1
        return "".join(out)
        