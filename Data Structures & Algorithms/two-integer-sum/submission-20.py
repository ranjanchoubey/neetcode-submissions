class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        # Approach 1 :  Brute Force
        for i in range(len(nums)):
            key = target-nums[i]
            for j in range(i+1,len(nums)):
                if nums[j] == key:
                    return[i,j]