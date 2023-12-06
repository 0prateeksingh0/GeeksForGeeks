class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        if not nums:
            return []
        
        c1, c2, count1, count2 = 0, 1, 0, 0
        
        for num in nums:
            if num == c1:
                count1 += 1
            elif num == c2:
                count2 += 1
            elif count1 == 0:
                c1, count1 = num, 1
            elif count2 == 0:
                c2, count2 = num, 1
            else:
                count1 -= 1
                count2 -= 1
        
        return [num for num in (c1, c2) if nums.count(num) > len(nums) // 3]