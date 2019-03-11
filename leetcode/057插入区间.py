# -*- coding:utf-8 -*-
__author__ = 'ShawDa'


# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution:
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[Interval]
        :type newInterval: Interval
        :rtype: List[Interval]
        """
        # 找到第一个interval.end>=new.start的位置
        loc = 0
        for i, interval in enumerate(intervals):
            if newInterval.start <= interval.end:
                break
            loc += 1
        intervals.insert(loc, newInterval)
        while loc < len(intervals) - 1:
            if intervals[loc].end >= intervals[loc+1].start:
                intervals[loc].start = min(intervals[loc].start, intervals[loc+1].start)
                intervals[loc].end = max(intervals[loc].end, intervals[loc+1].end)
                intervals.remove(intervals[loc+1])
            else:
                break
        return intervals
