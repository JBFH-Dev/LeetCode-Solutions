'''
Given an integer array arr, count how many elements x there are, such that x + 1 is also in arr. If there are duplicates in arr, count them separately.


'''

class Solution:
    def countElements(self, arr: List[int]) -> int:
        numsCount = {}
        for num in arr:
            if num in numsCount:
                numsCount[num] += 1
            else:
                numsCount[num] = 1
        
        total = 0
        for num in arr:
            if num+1 in numsCount:
                total += 1
        
        return total