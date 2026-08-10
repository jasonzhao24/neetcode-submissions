"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        sPtr,ePtr = 0,0
        starts = sorted([interval.start for interval in intervals])
        ends = sorted([interval.end for interval in intervals])
        rooms = 0
        max = 0
        while sPtr < len(starts):
            if starts[sPtr] < ends[ePtr]:
                rooms +=1
                sPtr +=1
            else:
                rooms -=1
                ePtr +=1
            if rooms > max:
                max = rooms    
        return max