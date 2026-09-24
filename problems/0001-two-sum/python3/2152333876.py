class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        hashmap={}

        for i,num in enumerate(nums):
            comp=target-num
            if comp in hashmap:
                return [i,hashmap[comp]]
            hashmap[num]=i
    