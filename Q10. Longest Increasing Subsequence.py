import bisect

class Solution:
    def lengthOfLIS(self, nums):
        sub = []
        for num in nums:
            pos = bisect.bisect_left(sub, num)
            if pos == len(sub):
                sub.append(num)
            else:
                sub[pos] = num
        return len(sub)
