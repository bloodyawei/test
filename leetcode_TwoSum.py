class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #k=0
        #for num in nums:
        #    k+=1
        #    if (target-num) in nums[k:]:
        #        return nums.index(num), nums[k:].index(target-num)+k
        for i in range(len(nums)):
            if (target-nums[i]) in nums[i+1:]:
                return i, nums[i+1:].index(target-nums[i])+(i+1)

