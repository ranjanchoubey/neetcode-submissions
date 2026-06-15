class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        nums.sort()
        n = len(nums)
        lst = []
        for i in range(n-2):
            a = nums[i]

            # skip a is positive then , No triplet after that
            if a > 0:
                break
            
            # skip duplicates
            if i !=0 and nums[i] == nums[i-1]:
                continue
            
            start = i + 1
            end = n - 1
            target = -a

            while(start < end):
                
                if nums[start] + nums[end] == target :
                    lst.append([a, nums[start],nums[end]])

                    start = start +1
                    end = end -1

                    # skip the duplicates to get different triplet
                    while start < end and  nums[start-1] == nums[start]:
                        start = start + 1
                    while start < end and nums[end] == nums[end+1]:
                        end  = end -1

                elif nums[start] + nums[end] > target :
                    end = end -1
                else:
                    start  = start +1
        return lst

                
            

