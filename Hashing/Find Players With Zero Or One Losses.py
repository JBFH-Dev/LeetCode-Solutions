'''
You are given an integer array matches where matches[i] = [winneri, loseri] indicates that the player winneri defeated player loseri in a match.

Return a list answer of size 2 where:

answer[0] is a list of all players that have not lost any matches.
answer[1] is a list of all players that have lost exactly one match.
The values in the two lists should be returned in increasing order.

Note:

You should only consider the players that have played at least one match.
The testcases will be generated such that no two matches will have the same outcome.
'''

from collections import defaultdict

class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        oneLoss = set()
        multiLoss = set()
        noLoss = set()

        for match in matches:
            if not match[0] in oneLoss and not match[0] in multiLoss:
                noLoss.add(match[0])
            if match[1] in noLoss:
                noLoss.remove(match[1])
                oneLoss.add(match[1])
            elif match[1] in oneLoss:
                oneLoss.remove(match[1])
                multiLoss.add(match[1])
            if not match[1] in oneLoss and not match[1] in multiLoss:
                oneLoss.add(match[1])
            
        return [sorted(list(noLoss)), sorted(list(oneLoss))]
        