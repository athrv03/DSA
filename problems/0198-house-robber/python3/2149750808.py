class Solution:
    def rob(self, nums: list[int]) -> int:
        rob1,rob2=0,0

        for num in nums:
            tmp=max(rob2,rob1+num)
            rob1=rob2
            rob2=tmp
        
        return rob2
