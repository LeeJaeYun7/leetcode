class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        maxResult = -1e9 

        N = len(nums)
        maxSum = [0]*N

        maxSum[0] = nums[0]

        for i in range(1, N):
            a = nums[i]
            b = maxSum[i-1] + nums[i]

            maxSum[i] = max(a, b)

        return max(maxSum) 
