def merge_descending(list1, start, end):  # O(n)
    mid = (start + end) // 2

    # The first sublist starts from start -> mid, the second sublist starts from mid+1 -> end
    merged_list = []

    index1 = start  # Keeps track of the elements added from the first sublist
    index2 = mid + 1  # Keeps track of the elements added from the second sublist

    while index1 <= mid and index2 <= end:

        if list1[index1]%2==0 and  list1[index2]%2==0:  # Reversed comparison for descending order
             #hon lfr2    ^
            if list1[index1]<list1[index2]:
                merged_list.append(list1[index1])  # Copying from the first sublist
                index1 += 1
            else:
                merged_list.append(list1[index2])  # Copying from the second sublist
                index2 += 1
        elif list1[index1] % 2 == 1 and list1[index2] % 2 == 1:
            if list1[index1] >= list1[index2]:
                merged_list.append(list1[index1])
                index1 += 1
            else:
                merged_list.append(list1[index2])
                index2 += 1
        elif list1[index1] % 2 == 0:
            merged_list.append(list1[index1])
            index1 += 1
        else:
            merged_list.append(list1[index2])
            index2 += 1

    while index1 <= mid:
        merged_list.append(list1[index1])  # Copy the remaining elements of the first sublist
        index1 += 1

    while index2 <= end:
        merged_list.append(list1[index2])  # Copy the remaining elements of the second sublist
        index2 += 1

    # Update the original list with the sorted descending list
    list1[start:end + 1] = merged_list

def mergesort_descending(list1, start, end):  # O(n*log(n)), n being the length of the list
    if start == end:  # Base case: sublist of length == 1
        return

    mid = (start + end) // 2
    mergesort_descending(list1, start, mid)  # Divide the list into two halves
    mergesort_descending(list1, mid + 1, end)

    merge_descending(list1, start, end)  # Merge the two halves in descending order

list1 = [2, 0, 3, 0, 10, -1, 6]
mergesort_descending(list1, 0, len(list1) - 1)
print(list1)