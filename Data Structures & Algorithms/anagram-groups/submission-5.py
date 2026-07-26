class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """
        strs = ["act","pots","tops","cat","stop","hat"]
        hash_s = {[]}
        for s in strs:  act
            c = [0]*26 c = [0...0]
            for i in s:        
                count[ord(i)-ord('a')]+=1
            hash_s[tuple(count)].append(s)
        return list(hash_s.values())

        act
        c=[1,0,1,0,0,...1]
        hash_s{(1,0,1,0,0.,.):"act"}
        (0,0,0,.1,1):"pots","tops"

        """
      
        hash_s = {}
        for s in strs:  
            c = [0]*26 
            for i in s:        
                c[ord(i)-ord('a')]+=1
            if tuple(c) not in hash_s:
                hash_s[tuple(c)]=[]
            hash_s[tuple(c)].append(s)
            
        return list(hash_s.values())
