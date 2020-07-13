from collections import defaultdict

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        #nums.sort()
        #if len(nums) == 1:
        #    return nums[0]
        #for i in range(len(nums)):
        #    if(i==0 and nums[0] != nums[1]):
        #        return nums[0]
        #    elif(i==len(nums)-1 and nums[i] != nums[i-1]):
        #        return nums[i]
        #    elif(nums[i] != nums[i-1] and nums[i] != nums[i+1]):
        #        return nums[i]
        hash_table = defaultdict(int)
        for i in nums:
            hash_table[i] += 1

        for i in hash_table:
            if hash_table[i] == 1:
                return i
