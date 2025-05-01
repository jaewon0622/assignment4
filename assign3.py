def trap_water(heights):
    n = len(heights)
    if n == 0:
        return 0

    left_max = [0] * n
    right_max = [0] * n

    # 왼쪽에서의 최대 높이
    left_max[0] = heights[0]
    for i in range(1, n):
        left_max[i] = max(left_max[i-1], heights[i])

    # 오른쪽에서의 최대 높이
    right_max[n-1] = heights[n-1]
    for i in range(n-2, -1, -1):
        right_max[i] = max(right_max[i+1], heights[i])

    # 각 위치에서 물이 담길 수 있는 양 계산
    trapped_water = 0
    for i in range(n):
        trapped_water += min(left_max[i], right_max[i]) - heights[i]

    return trapped_water

print(trap_water([0,1,0,2,1,0,1,3,2,1,2,1]))  # 6
print(trap_water([4,2,0,3,2,5]))             # 9
print(trap_water([1,0,2,1,0,1,3]))           # 5
