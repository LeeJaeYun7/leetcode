class Solution:

    answer = [] 
    total = [] 

    def __init__(self):
        self.answer = []  # 인스턴스 변수로 변경
        self.total = []  # 인스턴스 변수로 변경

    def findAnswer(self): 

       for tmp in self.total:
            stk = [] 
            isWellFormed = True
            for c in tmp:
                if c == '(':
                    stk.append(c)
                else:
                    if len(stk) == 0:
                        isWellFormed = False
                        break
                    stk.pop()
            
            if isWellFormed == False or len(stk) != 0:
                continue
            else:
                self.answer.append(tmp)


    def dfs(self, open, close, result):
        if open == 0 and close == 0:
            self.total.append(result)            
            return 

        if open != 0 and close != 0:
            for i in range(2):
                if i == 0:
                    result += '('
                    self.dfs(open-1, close, result)
                    result = result[:-1] 
                else:
                    result += ')'
                    self.dfs(open, close-1, result)
                    result = result[:-1]
        elif open == 0 and close != 0:
            result += ')'
            self.dfs(open, close-1, result)
            result = result[:-1]
        elif open != 0 and close == 0:
            result += '('
            self.dfs(open-1, close, result)
            result = result[:-1]

    def generateParenthesis(self, n: int) -> List[str]:
        
        result = "" 
        self.dfs(n, n, result)
        self.findAnswer() 
        return self.answer
