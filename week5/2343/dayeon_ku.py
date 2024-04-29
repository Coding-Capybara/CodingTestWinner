import sys

def binary_search(arr, m, left, right):
    answer = 0
    while left <= right:
        mid = (left + right) // 2
        temp = 0
        cnt = 1
        for num in arr:
            if temp + num > mid:
                temp = 0
                cnt += 1
            temp += num
        
        if cnt <= m:
            answer = mid
            right = mid - 1
        else:
            left = mid + 1

    return answer


n, m = map(int, input().split())
lecture_list = list(map(int, sys.stdin.readline().rstrip().split()))

left = max(lecture_list)
right = sum(lecture_list)

print(binary_search(lecture_list, m, left, right))