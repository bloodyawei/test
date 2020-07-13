class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        count=0
        output=[]
        for num in nums:
            count+=num
            output.append(count)
        return output