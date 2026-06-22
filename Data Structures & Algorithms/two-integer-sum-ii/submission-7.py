class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
       left = 0 
       right = len(numbers)-1
       while left<right:
           tar = numbers[left]+numbers[right]
           if tar == target:
                return [left+1,right+1]
           if tar<target:
              left+=1
           if tar>target:
               right-=1
       return []
               
      
        
