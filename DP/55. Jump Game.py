class Solution:
    def canJump(self, nums: List[int]) -> bool:

        N = len(nums)

        if N ==1:
            return True

        dp = [0]*N 

        num = nums[0]

        for i in range(1, num+1):
            if i <= N-1:
                dp[i] += 1 

        if dp[N-1] >= 1:
            return True 

        for i in range(1, N-1):
            num = nums[i]
            cnt = dp[i] 

            if cnt == 0:
                continue
            else:
                for j in range(i+1, i+num+1):
                    if j<=N-1:
                        dp[j] += cnt 

            if dp[N-1] >= 1:
                return True                 
        

        
