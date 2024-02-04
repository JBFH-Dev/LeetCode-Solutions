'''
You are given an integer array cards where cards[i] represents the value of the ith card. A pair of cards are matching if the cards have the same value.

Return the minimum number of consecutive cards you have to pick up to have a pair of matching cards among the picked cards. If it is impossible to have matching cards, return -1
'''

class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        lastSeenAt = {}
        minimum = len(cards) + 1
        for end in range(len(cards)):
            if cards[end] in lastSeenAt:
                minimum = min(minimum, end - lastSeenAt[cards[end]] + 1)
            lastSeenAt[cards[end]] = end
        
        if minimum == len(cards) + 1:
            return -1
        
        return minimum