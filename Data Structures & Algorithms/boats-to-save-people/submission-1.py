class Solution:
    def numRescueBoats(self, p: List[int], limit: int) -> int:
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


