# def binary_search(number_list, left_index, right_index, find_element):
#     #recursive
#     if left_index <= right_index:
#         middle_index = (left_index + right_index) // 2
#         if find_element == number_list[middle_index]:
#             return middle_index
#         elif find_element > number_list[middle_index]:
#             return binary_search(number_list, middle_index+1, right_index, find_element)
#         else:
#             return binary_search(number_list, left_index, middle_index-1, find_element)
#     else:   #not found
#         return -1

def binary_search(number_list, find_element):
    #iterative
    left_index = 0
    right_index = len(number_list)-1
    while left_index <= right_index:
        middle_index = (left_index + right_index) // 2
        if find_element == number_list[middle_index]:
            return middle_index
        elif find_element > number_list[middle_index]:
            left_index = middle_index+1
        else:
            right_index = middle_index-1
    return -1   #not found



number_list = [1, 2, 4, 6, 10, 11, 12]
find_element = 11
# print(binary_search(number_list, 0, len(number_list)-1, find_element))
print(binary_search(number_list, find_element))