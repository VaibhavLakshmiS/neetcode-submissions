import heapq
"""
y = 6
x = 4
 4<6
 diff = 2
"""
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heapq.heapify_max(stones)
        print(stones)
       
        while len(stones)>1:
            y = heapq.heappop_max(stones)
            print('y',y)

            x = heapq.heappop_max(stones)
            print('x',x)
            if x < y:
                diff = y-x
                print('diff',diff)
                heapq.heappush_max(stones,diff)
                print('after',stones)
        if len(stones)==1:
            return stones[0]
        else:
            return 0
            

