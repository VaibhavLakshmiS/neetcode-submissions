class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = {}
        for word in strs:
            sort_word = ''.join(sorted(word))
            if sort_word not in d:  
                d[sort_word] = [] 
            d[sort_word].append(word) 
        return list(d.values())  