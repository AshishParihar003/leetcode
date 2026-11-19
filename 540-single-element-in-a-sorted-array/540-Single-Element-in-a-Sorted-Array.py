class Solution(object):
    def singleNonDuplicate(self, nums):
        sum=0
        for i in nums:
            sum=sum^i
        return sum

        