class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        '''
         [t,t,t]
         c=[1,2,3]
         r = [[1,2,3]]

        '''
        res = []
        def dfs(cur,boolar):
            if False not in boolar:
                res.append(cur.copy())
                return 
            for i in range (len(boolar)):
                if boolar[i] == False:
                    cur.append(nums[i])
                    boolar[i] = True
                    dfs(cur,boolar)
                    cur.pop()
                    boolar[i]=False
                    

        boolar = [False]*len(nums)
        dfs([],boolar)
        return res

