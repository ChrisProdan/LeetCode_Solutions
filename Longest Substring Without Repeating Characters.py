class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        Hash_Map = dict()
        longest_Substring_Size = 1
        count = 0
        start_count = 0

        for char in s:
            if char not in Hash_Map:
                Hash_Map.update({char : count})
                count += 1
                if count - start_count > longest_Substring_Size:
                    longest_Substring_Size = count - start_count
            else:
                while(True):
                    if s[start_count] == char:
                        start_count += 1
                        count += 1                        
                        break
                    else:
                        Hash_Map.pop(s[start_count]) 
                        start_count += 1
            
        return longest_Substring_Size
                         



            
                



        