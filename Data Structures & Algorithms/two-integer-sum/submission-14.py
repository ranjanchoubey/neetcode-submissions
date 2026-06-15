class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # naive approach =O(n^2)
        # for i in range(len(nums)):
        #     for j in range(i+1,len(nums)):
        #         if nums[i]+nums[j] == target:
        #             return [i,j]

        # best approach
        dct = {}  # val -> index
        for i, n in enumerate(nums):
            diff = target - n
            if diff in dct:
                return [dct[diff], i]
            else :
                dct[n] = i
            






                            