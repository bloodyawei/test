
def mergeSort(nums):
    if len(nums) > 1 :
        left = mergeSort(nums[:len(nums)/2])
        right = mergeSort(nums[(len(nums)/2):])
        return merge(left, right)
    else :
        return nums
def merge(left, right):
    sortData = []
    leftIdx, rightIdx = 0, 0
    for i in range(len(left)+len(right)):
        if leftIdx == len(left):
            sortData.append(right[rightIdx])
            rightIdx += 1
        elif rightIdx == len(right):
            sortData.append(left[leftIdx])
            leftIdx += 1
        elif left[leftIdx] < right[rightIdx]:
            sortData.append(left[leftIdx])
            leftIdx += 1
        elif left[leftIdx] > right[rightIdx]:
            sortData.append(right[rightIdx])
            rightIdx += 1
    return sortData
if __name__ == '__main__' :
    print(mergeSort([54,26,93,17,1]))