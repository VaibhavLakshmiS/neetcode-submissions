class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        HashS={}
        HashT={}
        for i in range(len(s)):
            HashS[s[i]]=1+HashS.get(s[i],0) # finds the s[i] in S else returns 0 
            HashT[t[i]]=1+HashT.get(t[i],0)
        return HashS==HashT


        