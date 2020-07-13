class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        #nums.sort()
        #for i in range(len(nums)-1):
        #    if(nums[i+1]==nums[i]):
        #        return True
        #return False
        nums_set = set()
        nums_set.update(nums)
        if(len(nums_set)!=len(nums)):
            return True
        else:
            return False