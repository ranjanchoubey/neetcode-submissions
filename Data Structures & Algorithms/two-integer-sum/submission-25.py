class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        # Approach 1 :  Brute Force O(n^2)
        # for i in range(len(nums)):
        #     key = target-nums[i]
        #     for j in range(i+1,len(nums)):
        #         if nums[j] == key:
        #             return[i,j]

        # Approach 2 : Using Sorting O(nlogn)
        
        nums_with_index = list(enumerate(nums))
        nums_with_index.sort(key=lambda x : x[1])

        i = 0
        j = len(nums) - 1

        while(i<j):
            if nums_with_index[i][1] + nums_with_index[j][1] == target :
                return sorted([nums_with_index[i][0],nums_with_index[j][0]])
            elif nums_with_index[i][1] + nums_with_index[j][1] < target :
                i = i + 1
            else :
                j = j - 1


        



        
