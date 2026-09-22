class Solution:
    def search(self, nums: list[int], target: int) -> int:
        left=0

        while left<=right:
            mid=(left+right)//2

            if target>nums[mid]:
                left=mid+1
            elif target<nums[mid]:
                right=mid-1
            elif target==nums[mid]:
                return mid
        
        right=len(nums)-1
        return -1