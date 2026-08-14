class Solution:
    def numRescueBoats(self, p: List[int], limit: int) -> int:
        """
         people = [5,1,4,2], limit = 6
         5+2>6
         r-=1->
         5+4>6
         r-=1
         5+1==6
         []
        """
        
        p.sort()

        l,r = 0,len(p)-1
        boats = 0

        while l<=r:

            if p[l]+p[r] <= limit:
                l+=1
                r-=1

            else:
                r-=1

            boats+=1

        return boats


