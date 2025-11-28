
def merge_sort(arr):
    if len(arr)<=1:
        return arr

    mid=len(arr)//2
    left=arr[:mid]
    right=arr[mid:]

    left_sort=merge_sort(left)
    right_sort=merge_sort(right)

    return merge(left_sort,right_sort)

def merge(left,right):
    lp=rp=0

    arr=[]

    while lp<len(left) and rp<len(right):
        if left[lp]>right[rp]:
            arr.append(right[rp])
            rp+=1
        else:
            arr.append(left[lp])
            lp+=1

    if lp<len(left):
        arr.extend(left[lp:])

    if rp < len(right):
        arr.extend(right[rp:])

    return arr


# --- 示例 ---
if __name__ == "__main__":
    my_list = [38, 27, 43, 3, 9, 82, 10]
    print("Original list:", my_list)

    sorted_list = merge_sort(my_list)
    print("Sorted list:  ", sorted_list)
    # 更多测试用例
    test_cases = [
        [],
        [5],
        [9, 8, 7, 6, 5, 4, 3, 2, 1],
        [1, 1, 1, 1, 1],
        [5, 2, 8, 1, 9, 4, 6, 3, 7]
    ]

    for case in test_cases:
        print(f"\nSorting: {case}")
        print(f"Result:  {merge_sort(case)}")