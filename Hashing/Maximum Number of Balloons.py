'''
Given a string text, you want to use the characters of text to form as many instances of the word "balloon" as possible.

You can use each character in text at most once. Return the maximum number of instances that can be formed.
'''

from collections import defaultdict;
from math import floor;

class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        balloonCounter = {'b':0.0, 'a':0.0, 'l':0.0, 'o':0.0, 'n':0.0}
        doublesSet = set(['o','l'])
        for l in text:
            if l in balloonCounter:
                if not l in doublesSet:
                    balloonCounter[l] += 1.0
                else:
                    balloonCounter[l] += 0.5
        
        for i in doublesSet:
            balloonCounter[i] = floor(balloonCounter[i])
        
        minSeen = balloonCounter['b']
        for k in balloonCounter:
            if balloonCounter[k] < minSeen:
                minSeen = balloonCounter[k]
        
        return int(minSeen)