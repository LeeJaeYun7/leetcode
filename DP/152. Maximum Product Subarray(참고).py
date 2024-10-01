class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        
        if not nums:
            return 0
        
        # 초기값 설정
        max_prod = min_prod = result = nums[0]
        
        # nums의 두 번째 원소부터 순회
        for i in range(1, len(nums)):
            if nums[i] < 0:
                # 음수일 경우 최대값과 최소값을 바꿔야 함 (음수를 곱하면 값이 반전되기 때문)
                max_prod, min_prod = min_prod, max_prod
            
            # 현재 값을 포함하는 최대 곱과 최소 곱 갱신
            max_prod = max(nums[i], max_prod * nums[i])
            min_prod = min(nums[i], min_prod * nums[i])
            
            # 결과 업데이트
            result = max(result, max_prod)
        
        return result
