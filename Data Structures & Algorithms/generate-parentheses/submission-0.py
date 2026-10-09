class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        def dfs (ope,close,subset):
            if ope == close == n:
                res.append("".join(subset))
                return
            if ope<n:
                subset.append('(')
                dfs(ope+1,close,subset)
                subset.pop()
            if close<ope:
                subset.append(')')
                dfs(ope,close+1,subset)
                subset.pop()
            
          
        dfs(0,0,[])   
        return res
           