class Solution:
    def countAndSay(self, n: int) -> str:
        def RLE(num: str) -> str:
            output = ""
            while(len(num) > 0):
                curnum = num[0]
                num = num[1:]
                count = 1
                while(len(num) > 0 and num[0] == curnum):
                    count += 1
                    num = num[1:]
                output += str(count) + curnum
            
            return output
            
        curOutput = "1"
        for i in range(n-1):
            curOutput = RLE(curOutput)
        
        return curOutput


        