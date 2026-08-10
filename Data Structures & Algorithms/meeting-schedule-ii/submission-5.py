"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        sPtr,ePtr = 0,0 ## Starting pointers of start and end
        # Sorting
        starts = sorted([interval.start for interval in intervals])
        ends = sorted([interval.end for interval in intervals])
        rooms = 0
        max = 0
        # Keep going until we reach the amount of meetings
        while sPtr < len(starts):
            if starts[sPtr] < ends[ePtr]: ## If the end time is greater than the starting time, this means that we have to create a new room
                rooms +=1
                sPtr +=1
            else: ## Otherwise, it means that we have a new empty room from meetings that don't need an extra room and don't conflict with each other
                rooms -=1
                ePtr +=1
            if rooms > max: 
                max = rooms    
        return max