class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        return [(i,i2) for i in range(len(nums)) for i2 in range(i+1,len(nums)) if nums[i]+nums[i2] == target][0]
