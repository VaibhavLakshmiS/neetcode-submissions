class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hash_s={}
        for s in strs:
            c = [0]*26
            for i in s:
                c[ord(i)-ord('a')]+=1
            if tuple(c) not in hash_s:
                hash_s[tuple(c)]=[]
            hash_s[tuple(c)].append(s)
        return list(hash_s.values())
                 
