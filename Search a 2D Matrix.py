class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        width = len(matrix[0])
        height = len(matrix)


        # first find what matrix it is in
        lp = 0
        rp = height - 1
        mp = (rp + lp) // 2 
        row = -1
        
        while lp < rp:
            if matrix[mp][0] <= target and (mp == height - 1 or matrix[mp+1][0] > target):
                row = mp
                break
            elif matrix[mp][0] > target:
                rp = mp - 1
            else:
                lp = mp + 1
            
            mp = (rp + lp) // 2
        
        if row == -1:
            if matrix[lp][0] <= target and (lp == height - 1 or matrix[lp+1][0] > target):
                row = lp
            else:
                return False
        
        # Now perform binary search within the row

        nums = matrix[row]

        lp = 0
        rp = width - 1
        mp = (rp + lp) // 2 
        
        while lp < rp:
            if nums[mp] == target:
                return True
            elif nums[mp] > target:
                rp = mp - 1
            else:
                lp = mp + 1
            
            mp = (rp + lp) // 2
        
        if nums[lp] == target:
            return True
        else:
            return False
        