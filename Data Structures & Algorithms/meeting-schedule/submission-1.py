"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals_new = sorted(intervals,key = lambda x:x.start)
        ptr = 0 
        nxt = 1
        while ptr<len(intervals_new) and nxt<len(intervals_new):
            if intervals_new[ptr].end>intervals_new[nxt].start:
                return False
            ptr=ptr+1
            nxt=nxt+1
        return True