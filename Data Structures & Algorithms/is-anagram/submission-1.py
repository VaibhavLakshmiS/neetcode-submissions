class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        shas={}
        thas={}
        if len(s)!=len(t):
            return False
        for i in range (len(s)):
            shas[s[i]]=1+shas.get(s[i],0)
            thas[t[i]]=1+thas.get(t[i],0)
        return shas == thas