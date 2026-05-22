class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        start = 0
        end = len(numbers)-1
        index=[]
        
        while start<end:
            tot = numbers[start]+numbers[end]
            if tot == target:
                return [start+1,end+1]
            if tot>target:
                end-=1
            if tot<target:
                start+=1
