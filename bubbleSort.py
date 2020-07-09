def bubbleSort(n_lst):
    n = len(n_lst)
    for i in range(n):
        for j in range(0, n-i-1):
            if n_lst[j] > n_lst[j+1]:
                n_lst[j], n_lst[j+1] = n_lst[j+1], n_lst[j]
    return n_lst

if __name__ == "__main__":
    n_lst = [6,5,4,3,2,1]
    print(bubbleSort(n_lst))