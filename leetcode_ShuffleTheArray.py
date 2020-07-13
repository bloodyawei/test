class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        output = []
        nums1 = nums[:n]
        nums2 = nums[n:]
        for i in range(n):
            output.append(nums1[i])
            output.append(nums2[i])
        return output
