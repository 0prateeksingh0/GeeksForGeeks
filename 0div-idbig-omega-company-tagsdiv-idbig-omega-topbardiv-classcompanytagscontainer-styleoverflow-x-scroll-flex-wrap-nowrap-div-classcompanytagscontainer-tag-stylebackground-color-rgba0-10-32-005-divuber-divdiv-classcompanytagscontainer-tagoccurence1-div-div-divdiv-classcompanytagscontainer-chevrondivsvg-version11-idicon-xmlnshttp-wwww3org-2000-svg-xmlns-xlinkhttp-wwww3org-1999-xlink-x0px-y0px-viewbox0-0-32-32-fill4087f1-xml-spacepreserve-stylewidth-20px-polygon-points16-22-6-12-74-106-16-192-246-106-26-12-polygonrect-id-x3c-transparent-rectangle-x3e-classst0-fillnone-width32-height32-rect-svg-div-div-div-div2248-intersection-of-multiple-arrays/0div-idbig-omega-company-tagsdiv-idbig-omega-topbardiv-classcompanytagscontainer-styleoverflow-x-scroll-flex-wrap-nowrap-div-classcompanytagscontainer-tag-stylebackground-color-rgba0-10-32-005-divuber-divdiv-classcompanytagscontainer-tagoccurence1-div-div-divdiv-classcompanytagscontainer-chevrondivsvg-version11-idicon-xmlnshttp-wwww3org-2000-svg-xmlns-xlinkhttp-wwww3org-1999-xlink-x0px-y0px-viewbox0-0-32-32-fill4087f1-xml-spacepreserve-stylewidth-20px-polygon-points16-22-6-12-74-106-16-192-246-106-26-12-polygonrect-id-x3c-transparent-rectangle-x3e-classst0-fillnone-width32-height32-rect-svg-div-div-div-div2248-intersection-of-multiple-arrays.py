class Solution:
    def intersection(self, nums: List[List[int]]) -> List[int]:
        initi=set(nums[0])
        for i in range(1,len(nums)):
            initi=initi.intersection(set(nums[i]))
        initi=sorted(list(initi))
        return initi
                   
