class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        output = []
        if(len(nums1) <= len(nums2)):
            for num in nums1:
                if num in nums2:
                    output.append(num)
                    nums2.remove(num)
        else:
            for num in nums2:
                if num in nums1:
                    output.append(num)
                    nums1.remove(num)
        return output


