class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        '''
        n= [ 1,1,3,4]
        t = 2
         r = 1
         l = 1 
         l+r = 2
        '''

        left = 0
        right = len(numbers)-1
        while left<right:
                val = numbers[left]+numbers[right]
                if val == target:
                        return [left+1,right+1]
                if val>target:
                        right-=1
                else:
                     left+=1
        return []

               