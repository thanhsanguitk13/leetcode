from typing import List
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        l=1
        
        for r in range(1,len(nums)):
            if nums[r] != nums[r-1]:
                nums[l] = nums[r]
                l += 1
        return l
    
# Example usage:
solution = Solution()
nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
print('length of nums: ',len(nums))
k = solution.removeDuplicates(nums)
print(k)  # Output: 5
print(nums[:k])  # Output: [0, 1, 2, 3, 4]
