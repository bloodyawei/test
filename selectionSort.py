def selectionSort(nums):
    for i in range(len(nums)):
        minIdx = i
        for j in range(i+1, len(nums)):
            if nums[minIdx] > nums[j]:
                minIdx = j
        nums[i], nums[minIdx] = nums[minIdx], nums[i]
    return nums # [17, 20, 26, 31, 44, 54, 55, 77, 93]

if __name__ == '__main__' :
    print(selectionSort([54,26,93,17,77,31,44,55,20]))