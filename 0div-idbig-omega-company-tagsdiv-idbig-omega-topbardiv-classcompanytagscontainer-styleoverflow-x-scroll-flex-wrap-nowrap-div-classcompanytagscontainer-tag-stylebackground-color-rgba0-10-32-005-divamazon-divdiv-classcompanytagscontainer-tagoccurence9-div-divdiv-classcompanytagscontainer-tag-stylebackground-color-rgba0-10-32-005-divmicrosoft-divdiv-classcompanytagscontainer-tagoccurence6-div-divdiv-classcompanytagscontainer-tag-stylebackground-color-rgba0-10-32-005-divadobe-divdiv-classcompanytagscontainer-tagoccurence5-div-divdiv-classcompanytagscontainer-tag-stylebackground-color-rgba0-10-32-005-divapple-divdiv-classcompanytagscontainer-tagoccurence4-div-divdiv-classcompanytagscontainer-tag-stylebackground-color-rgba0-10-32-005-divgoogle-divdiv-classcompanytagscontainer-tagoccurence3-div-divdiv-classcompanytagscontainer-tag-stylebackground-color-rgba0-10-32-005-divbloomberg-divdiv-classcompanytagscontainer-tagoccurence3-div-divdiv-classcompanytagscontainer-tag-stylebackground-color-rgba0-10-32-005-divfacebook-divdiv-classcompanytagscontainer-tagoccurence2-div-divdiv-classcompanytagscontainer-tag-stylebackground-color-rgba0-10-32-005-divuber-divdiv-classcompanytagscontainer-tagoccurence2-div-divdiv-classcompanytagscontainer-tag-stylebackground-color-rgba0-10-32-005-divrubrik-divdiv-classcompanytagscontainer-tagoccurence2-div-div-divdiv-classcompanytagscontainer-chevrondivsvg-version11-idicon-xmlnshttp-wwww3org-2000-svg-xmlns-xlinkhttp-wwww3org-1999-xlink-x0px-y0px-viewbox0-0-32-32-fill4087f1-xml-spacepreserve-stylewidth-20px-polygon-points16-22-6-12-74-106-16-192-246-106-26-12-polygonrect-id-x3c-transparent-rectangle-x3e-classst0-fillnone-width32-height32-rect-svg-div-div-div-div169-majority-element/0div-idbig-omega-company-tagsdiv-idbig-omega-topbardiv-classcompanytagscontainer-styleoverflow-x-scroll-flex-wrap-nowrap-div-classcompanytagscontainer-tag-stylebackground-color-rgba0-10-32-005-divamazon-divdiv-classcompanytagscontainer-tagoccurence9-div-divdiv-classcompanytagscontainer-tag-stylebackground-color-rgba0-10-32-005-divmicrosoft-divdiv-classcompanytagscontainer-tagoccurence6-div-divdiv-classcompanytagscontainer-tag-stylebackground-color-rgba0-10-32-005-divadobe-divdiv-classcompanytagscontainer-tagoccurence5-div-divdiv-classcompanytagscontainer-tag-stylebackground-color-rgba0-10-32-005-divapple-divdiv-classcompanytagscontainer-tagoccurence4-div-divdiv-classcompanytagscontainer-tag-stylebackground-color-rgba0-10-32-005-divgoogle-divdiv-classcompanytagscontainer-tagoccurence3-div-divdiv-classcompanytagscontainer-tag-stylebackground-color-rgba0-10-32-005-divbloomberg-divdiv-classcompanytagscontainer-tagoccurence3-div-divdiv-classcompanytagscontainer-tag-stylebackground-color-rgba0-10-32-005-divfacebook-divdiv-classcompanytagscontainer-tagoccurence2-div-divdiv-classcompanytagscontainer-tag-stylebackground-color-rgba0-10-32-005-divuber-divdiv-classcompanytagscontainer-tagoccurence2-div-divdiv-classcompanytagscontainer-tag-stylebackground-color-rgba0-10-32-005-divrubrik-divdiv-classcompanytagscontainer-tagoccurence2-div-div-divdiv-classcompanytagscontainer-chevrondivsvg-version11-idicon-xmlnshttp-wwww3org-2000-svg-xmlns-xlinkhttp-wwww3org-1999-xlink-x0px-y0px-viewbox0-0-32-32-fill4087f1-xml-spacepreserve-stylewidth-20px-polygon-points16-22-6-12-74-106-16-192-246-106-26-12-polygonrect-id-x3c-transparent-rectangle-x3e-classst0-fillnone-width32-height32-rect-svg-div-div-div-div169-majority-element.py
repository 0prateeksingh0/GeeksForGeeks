class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = 0
        c = None
        for num in nums:
            if count == 0:
                c = num
            count += (1 if num == c else -1)
        return c
    
    
    