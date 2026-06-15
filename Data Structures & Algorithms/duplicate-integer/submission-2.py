class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        return False if len(set(nums))==len(list(nums)) else True
         