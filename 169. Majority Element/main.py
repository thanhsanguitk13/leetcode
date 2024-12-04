from typing import List

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        res = 0
        count = 0
        for n in nums:
            if count == 0:
                res = n
            count += (1 if n ==res else -1)
        return res
solution = Solution()
print(solution.majorityElement([3, 2, 3])) 
print(solution.majorityElement([2, 2, 1, 1, 1, 2, 2]))  
