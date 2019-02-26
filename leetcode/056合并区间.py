# -*- coding:utf-8 -*-
__author__ = 'ShawDa'


# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution:
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        intervals.sort(key=lambda x: (x.start, x.end))
        i = 1
        while i < len(intervals):
            if intervals[i].start <= intervals[i-1].end:
                intervals[i-1].end = max(intervals[i-1].end, intervals[i].end)
                intervals.remove(intervals[i])
            else:
                i += 1
        return intervals
