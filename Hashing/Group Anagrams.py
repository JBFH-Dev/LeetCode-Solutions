'''
Given an array of strings strs, group the anagrams together. You can return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.
'''

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        angramMap = {}
        for s in strs:
            sorts = ''.join(sorted(s))
            if sorts in angramMap:
                angramMap[sorts].append(s)
            else:
                angramMap[sorts] = [s]
            
        return angramMap.values()
        