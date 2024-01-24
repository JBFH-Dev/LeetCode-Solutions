# Given a 0-indexed string word and a character ch, reverse the segment of word that starts at index 0 and ends at the index of the first occurrence of ch (inclusive). If the character ch does not exist in word, do nothing.

class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
    
        arr = list(word)
        start = 0
        end = 0
        while end < len(arr) and not arr[end] == ch:
            end += 1
        if end == len(arr):
            return word
        while start < end:
            arr[start], arr[end] = arr[end], arr[start]
            start += 1
            end -= 1
        return ''.join(arr)