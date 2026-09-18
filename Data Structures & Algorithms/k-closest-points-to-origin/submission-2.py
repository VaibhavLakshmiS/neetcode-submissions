class Solution:

    '''
     key = coordinates
     val = euclid dist

     points = {(0,2):2,(2,0):2,(2,2):2.8}




    '''
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        hash_pts = {}
        e_dlist = []
        res = []
        for i in points:
            x = i[0]
            y = i[1]
            e_d = math.sqrt((0-x)**2 + (0-y)**2)
            e_dlist.append(e_d)
            hash_pts[tuple(i)] = e_d
        heapq.heapify(e_dlist)
        for i in range(k):
            val = heapq.heappop(e_dlist)
            keys = [k for k, v in hash_pts.items() if v == val]
            hash_pts.pop(keys[0])
            res.append(list(keys[0]))
        return res
        
        
        
            