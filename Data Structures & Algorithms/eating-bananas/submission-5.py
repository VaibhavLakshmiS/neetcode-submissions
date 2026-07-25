import math 
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        """
        piles = [1,4,3,2], h = 9
        k = [1,2,3,4]
        l = 1
        r = 1
        k = 2
        hours = 0
        1/2+4/2+3/2+2/2 = 6

        piles=[3,6,7,11]
        k = [ 1,2,3,4,5,6,7,8,9,10,11]
        l = 4
        r = 5
        k = 3
        res = 5
        hours =3/3+6/3+7/3+11/3=1+2+3+4= 10
        h=8

        k=4
        hours= 3/4+6/4+7/4+11/4 = 1+2+2+3=8



        """

        l,r = 1 , max(piles)
        res = r #11
        while l<=r:
            k = (l+r)//2 
            hours = 0 
            for i in range(len(piles)):
                hours+=math.ceil(piles[i]/k)
            if hours <= h:
                res = min(res,k)
                r = k-1
                
            else: 
                l = k+1
        return res
            


            

