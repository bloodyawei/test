def insertionSort(nums):
    for i in range(1, len(nums)) :
        j, fixed = i-1, nums[i]
        while j >=0 and nums[j] > fixed:
            nums[j+1] = nums[j]
            j -= 1
        nums[j+1] = fixed
    return nums

if __name__ == '__main__' :
    print(insertionSort([54,26,93,17,77,31,44,55,20]))