class Solution:
    def generateMatrix(self, n: int) -> list[list[int]]:
        matrix = [[0] * n for __ in range(n)]

        width = n
        height = n
        def spiralMaker(prevMove: str, x: int, y: int, count: int):
            if(x == width or x == -1 or y == -1 or y == height or matrix[y][x] != 0):
                return
            matrix[y][x] = count
            if prevMove == "right":
                if x == width-1 or matrix[y][x+1] != 0:
                    spiralMaker("down",x,y+1,count + 1)
                else:
                    spiralMaker("right",x+1,y,count + 1)
            elif prevMove == "down":
                if y == height-1 or matrix[y+1][x] != 0:
                    spiralMaker("left",x-1,y,count + 1)
                else:
                    spiralMaker("down",x,y+1,count + 1)
            elif prevMove == "left":
                if x == 0 or matrix[y][x-1] != 0:
                    spiralMaker("up",x,y-1,count + 1)
                else:
                    spiralMaker("left",x-1,y,count + 1)
            else:
                if y == 0 or matrix[y-1][x] != 0:
                    spiralMaker("right",x+1,y,count + 1)
                else:
                    spiralMaker("up",x,y-1,count + 1)
        
        spiralMaker("right",0,0,1)
        return matrix
        