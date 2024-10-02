class Solution:
    def numDecodings(self, s: str) -> int:

        N = len(s)
        dp = [0]*len(s)    

        if s[0] == '0':
            return 0 

        if len(s) == 1:
            if s == '0':
                return 0
            else:
                return 1 
        elif len(s) == 2:
            if s[0] != "0":
                dp[0] = 1

            for i in range(1, 2):
                num1 = s[i]
                num2 = s[i-1:i+1]
                if 1<= int(num1) and int(num1) <= 9:
                    dp[1] += 1

                if 10<= int(num2) and int(num2) <= 26:
                    dp[1] += 1
        else:
            if s[0] != "0":
                dp[0] = 1

            for i in range(1, 2):
                num1 = s[i]
                num2 = s[i-1:i+1]
                if 1<= int(num1) and int(num1) <= 9:
                    dp[1] += 1

                if 10<= int(num2) and int(num2) <= 26:
                    dp[1] += 1

            for i in range(2, N):
                num1 = s[i]
                num2 = s[i-1:i+1]

                if 1<= int(num1) and int(num1) <= 9:
                    dp[i] += dp[i-1]

                if 10<= int(num2) and int(num2) <= 26:
                    dp[i] += dp[i-2]
                        
        return dp[N-1]
        
        

