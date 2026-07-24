class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row = len(matrix) 
        col = len(matrix[0]) #4 n 
        for i in range(row):
            l = 0
            r = len(matrix[i])-1
            while l<=r:
                mid = (l+r)+1//2 
                if matrix[i][mid] == target:
                    return True

                if matrix[i][mid]< target: 
                    l = mid+1 
                

                else:
                    r = mid-1  
        return False        

