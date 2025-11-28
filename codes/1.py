import bisect

# 读取测试数据组数
T = int(input())

for _ in range(T):
    # 读取天数
    n = int(input())

    # 读取每天的失误次数
    mistakes = list(map(int, input().split()))

    # 初始能力值为0
    ability = 0
    max_ability = 0

    # 维护一个有序列表，存储之前所有天的失误次数
    sorted_previous = []

    # 从第二天开始计算（第一天不改变能力值）
    for day in range(n):
        if day > 0:
            # 使用二分查找找到有多少天失误次数 < mistakes[day]
            less = bisect.bisect_left(sorted_previous, mistakes[day])

            # 之前总天数
            total_previous = len(sorted_previous)

            # 有多少天失误次数 > mistakes[day]
            greater = total_previous - bisect.bisect_right(sorted_previous, mistakes[day])

            # 能力值变化 = less - greater
            change = less - greater
            ability += change

            # 更新最大能力值
            max_ability = max(max_ability, ability)

        # 将当前天的失误次数插入有序列表
        bisect.insort(sorted_previous, mistakes[day])

    # 输出最大能力值和最终能力值
    print(max_ability, ability)