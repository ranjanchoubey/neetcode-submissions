class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        # Method1 : Using Sorting ; Time Complexity = O(nlogn)
        sorted_s = "".join(sorted(s))
        sorted_t = "".join(sorted(t))        
        # if sorted_s == sorted_t :
        #     return True
        # else :
        #     return False
        return True if sorted_s == sorted_t  else False