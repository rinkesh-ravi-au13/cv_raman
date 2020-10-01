class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        for i in range(len(nums)):
            if nums[i]==target:
                return i
            else:
                if target<nums[i] and target>nums[i-1]:
                    return i
                elif target>nums[-1]:
                    return len(nums)
                elif target<nums[0]:
                    return 0