class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        list1=[]
        for i in range(len(nums)):
            if nums[i]== target:
                list1.append(i)
        return list1