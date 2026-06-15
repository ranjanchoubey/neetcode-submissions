class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        """ Approach 1 :  Brute Force O(n^2) """
        # for i in range(len(nums)):
        #     key = target-nums[i]
        #     for j in range(i+1,len(nums)):
        #         if nums[j] == key:
        #             return[i,j]

        """ Approach 2 : Using Sorting O(nlogn) """
        # lst = list(enumerate(nums))
        # lst.sort(key=lambda x : x[1])
        # i = 0
        # j = len(nums) - 1
        # while(i<j):
        #     if lst[i][1] + lst[j][1] == target :
        #         return sorted([lst[i][0],lst[j][0]]) # return the list in sorted order
        #     elif lst[i][1] + lst[j][1] < target :
        #         i = i + 1
        #     else :
        #         j = j - 1

        """ Approach 3 : Hash Map O(n) time - Optimal """
        # step1. Build Hash map in one scan, because search key in O(1) time
        # store index as value and number as key
        dct = {}
        for i in range(len(nums)):
            dct[nums[i]] = i

        # step2. Use Hash map 
        for i in range(len(nums)):
            pair = target-nums[i]
            if pair in dct and dct[pair] != i:
                return [i,dct.get(pair)]
                    



        



        
