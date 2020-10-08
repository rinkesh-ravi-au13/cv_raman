

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        dp = [0] * len(nums)
        dp[-1] = len(nums)-1
        for i in range(len(nums)-2,-1,-1):
            dp[i] = max(dp[i:i+nums[i]+1])
        return dp[0] >= len(nums)-1