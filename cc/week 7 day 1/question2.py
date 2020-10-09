#question2 :- https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/


class Solution:
    def findMin(self, nums: List[int]) -> int:
        nums.sort()
        return nums[0]