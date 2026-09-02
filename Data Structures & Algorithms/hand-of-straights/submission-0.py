class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False
        map = {}
        hand.sort()
        for card in hand:
            if card not in map:
                map[card] = 1
            else:
                map[card]+=1
        for card in hand:
            if map[card] > 0:
                for i in range(groupSize):
                    if map.get(card + i, 0) > 0:
                        map[card + i] -= 1
                    else:
                        return False
        return True
