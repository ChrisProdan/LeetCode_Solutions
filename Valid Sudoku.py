class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        Rows = [{},{},{},{},{},{},{},{},{}]
        Columns = [{},{},{},{},{},{},{},{},{}]
        Boxes = [{},{},{},{},{},{},{},{},{}]

        Row_Count = 0
        Column_Count = 0
        for r in board:
            for x in r:
                Board = (Row_Count // 3)*3 + (Column_Count // 3)

                if x == ".":
                    x = "."
                elif x in Rows[Row_Count] or x in Columns[Column_Count] or x in Boxes[Board]:
                    return False
                else:
                    Rows[Row_Count][x] = 0
                    Columns[Column_Count][x] = 0
                    Boxes[Board][x] = 0
                
                Column_Count = Column_Count + 1 if Column_Count != 8 else 0
            
            Row_Count += 1
        
        return True
        