class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res =[]
        candidates.sort()
        def dfs(i,cur,tot):
            if tot == target:
                res.append(cur.copy())
                return
            if tot>target or i == len(candidates):
                return
            cur.append(candidates[i])
            dfs(i+1,cur,tot+candidates[i])
            cur.pop()
            while i+1<len(candidates) and candidates[i] == candidates[i+1]:
                i = i+1
            dfs(i+1,cur,tot)
        dfs(0,[],0)
        return res

