# 1. 传统方法
def partition(array,low,high):
    """
       该函数选取最后一个元素作为基准，将所有小于基准的元素放在基准的左边，
       所有大于基准的元素放在基准的右边。
       """
    # 选取最后一个元素作为基准
    pivot = array[high]

    # i 指向较小元素的边界
    i = low - 1

    for j in range(low, high):
        if array[j] <= pivot:
            # 如果当前元素小于或等于基准，则将其与 i 指向的下一个位置交换
            i = i + 1
            (array[i], array[j]) = (array[j], array[i])

    # 将基准元素放到正确的位置
    (array[i + 1], array[high]) = (array[high], array[i + 1])

    # 返回基准元素的索引
    return i + 1

def quick_sort_1(array,low,high):
    if low<high:
        pivot = partition(array, low, high)

        quick_sort_1(array, low, pivot - 1)
        quick_sort_1(array, pivot + 1, high)



def quick_sort_2(array):
    if len(array)<=1:
        return array
    else:
        pivot=array[len(array)//2]

        left=[x for x in array if x<pivot]
        right=[x for x in array if x>pivot]
        middle=[x for x in array if x==pivot]

        return quick_sort_2(left)+middle+quick_sort_2(right)


if __name__ == '__main__':
    # 示例
    data = [8, 7, 2, 1, 0, 9, 6]
    print("未排序的数组:")
    print(data)

    # # 1. 传统快排
    # quick_sort_1(data,0,len(data)-1)
    # print("排序后的数组:")
    # print(data)

    # # 2. 基于 pythonic 优化
    print("排序后的数组:")
    print(quick_sort_2(data))
