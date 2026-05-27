class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        for i in range(0,len(s2)-len(s1)+1):
            window = s2[i:i+len(s1)]
            if sorted(window) == sorted(s1):
                return True
        return False
            
        
             
        