class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # naive approach =O(n^2)
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i]+nums[j] == target:
                    return [i,j]

        # best approch : using 2 pointer O(n)
        start = 0
        end = len(nums)-1
        while(i>j):
            summ  = nums[start]+nums[end]
            if summ ==target:
                return [start,end]

            elif summ < target:
                start += 1
            else:
                end -= 1



                            