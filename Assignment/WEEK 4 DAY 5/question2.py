#Q2. Write a Python program to remove the K'th element from a given list, print the new list.
#Original list:
#[1, 1, 2, 3, 4, 4, 5, 1]
#Length of the first part of the list: 3
#Splited the said list into two parts:
#([1, 1, 2], [3, 4, 4, 5, 1])

def remove_kth_element(n_list, L):
    return  n_list[:L-1] + n_list[L:]

n_list = [1,1,2,3,4,4,5,1]
print("Original list:") 
print(n_list)
kth_position = 3
result = remove_kth_element(n_list, kth_position)
print("\nAfter removing an element at the kth position the list now is:")
print(result)