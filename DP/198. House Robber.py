class Solution:
    def rob(self, nums: List[int]) -> int:

        N = len(nums)
        dp = [[0]*2 for _ in range(N)]

        dp[0][1] = nums[0]
        dp[0][0] = 0
        maxResult = max(dp[0][1], dp[0][0])

        for i in range(1, N):
            dp[i][1] = dp[i-1][0]+nums[i]
            dp[i][0] = max(dp[i-1][1], dp[i-1][0])
        
            maxResult = max(maxResult, dp[i][1])
            maxResult = max(maxResult, dp[i][0])
        
        return maxResult 
