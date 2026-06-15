class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # naive approach =O(n^2)
        # for i in range(len(nums)):
        #     for j in range(i+1,len(nums)):
        #         if nums[i]+nums[j] == target:
        #             return [i,j]

        # best approach
        dct = {}  # val -> index
        for index, value in enumerate(nums):
            diff = target - value
            if diff in dct.keys():
                return [dct[diff], index]
            else :
                dct[value] = index
            






                            