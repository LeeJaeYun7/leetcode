class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        
        N = len(nums)
        dp = [0]*N

        for i in range(N):
            dp[i] += 1 

        for i in range(N):
            for j in range(i):
                if (nums[j] < nums[i]) and (dp[j] == dp[i]):
                    dp[i] += 1 
        
        return max(dp)
