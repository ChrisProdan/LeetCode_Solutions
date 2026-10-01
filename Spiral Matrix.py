class Solution:
    def spiralOrder(self, matrix: list[list[int]]) -> list[int]:
        Output = []
        width = len(matrix[0])
        height = len(matrix)
        def spiralMaker(prevMove: str, x: int, y: int):
            if(x == width or x == -1 or y == -1 or y == height or matrix[y][x] == "#"):
                return
            Output.append(matrix[y][x])
            matrix[y][x] = "#"
            if prevMove == "right":
                if x == width-1 or matrix[y][x+1] == "#":
                    spiralMaker("down",x,y+1)
                else:
                    spiralMaker("right",x+1,y)
            elif prevMove == "down":
                if y == height-1 or matrix[y+1][x] == "#":
                    spiralMaker("left",x-1,y)
                else:
                    spiralMaker("down",x,y+1)
            elif prevMove == "left":
                if x == 0 or matrix[y][x-1] == "#":
                    spiralMaker("up",x,y-1)
                else:
                    spiralMaker("left",x-1,y)
            else:
                if y == 0 or matrix[y-1][x] == "#":
                    spiralMaker("right",x+1,y)
                else:
                    spiralMaker("up",x,y-1)
        
        spiralMaker("right",0,0)
        return Output


        