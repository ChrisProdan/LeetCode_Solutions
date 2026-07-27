class Solution:
    def findMin(self, nums: List[int]) -> int:
        

        low = 0
        high = len(nums) - 1


        while True:
            mid = low + (high - low) // 2
            if high - low < 3:
                return min(nums[low:high+1])
            elif (mid == 0 and nums[mid] < nums[mid+1] and nums[mid] < nums[-1]) or (mid == len(nums) - 1 and nums[mid] < nums[mid-1] and nums[mid] < nums[0]) or (nums[mid] < nums[mid+1] and nums[mid] < nums[mid-1]):
                return nums[mid]
            elif (low == 0 and nums[low] < nums[low+1] and nums[low] < nums[-1]) or (low == len(nums) - 1 and nums[low] < nums[low-1] and nums[low] < nums[0]) or (nums[low] < nums[low+1] and nums[low] < nums[low-1]):
                return nums[low]
            elif nums[low] < nums[mid]:
                low = mid + 1
            else:
                high = mid - 1
            

        