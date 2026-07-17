class Solution:
    def maxArea(self, height: List[int]) -> int:
        P_Left = 0
        P_Right = len(height) - 1
        max_Water = 0
        while P_Left < P_Right:
            if (P_Right - P_Left) * (min(height[P_Left], height[P_Right])) > max_Water:
                max_Water = (P_Right - P_Left) * (min(height[P_Left], height[P_Right]))

            if height[P_Left] < height[P_Right]:
                P_Left += 1
            else:
                P_Right -= 1
        
        return max_Water
            

        