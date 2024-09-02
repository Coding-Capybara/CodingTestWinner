'''
효율성 아예 패스 x
정확성 전부 패스
'''
# def solution(stones, k):
#     answer = 0
#     consec = 0
    
#     while True:
#         for idx in range(len(stones)):
#             if stones[idx] != 0:
#                 stones[idx] -= 1
#                 consec = 0
#             else:
#                 consec += 1
                
#             if consec == k:
#                 return answer
                
#         consec = 0
#         answer += 1

def solution(stones, k):
    # 몇명의 니니즈 친구들이 건널 수 있을지 이진탐색으로 탐색
    return binary_search(stones, k, 1, 200000000)

def binary_search(arr, k, left, right):    
    while left <= right:
        temp = arr.copy()
        mid = (left + right) // 2 # 만약 중간값인 mid명의 니니즈 친구들이 건널 수 없다면 최대값을 줄이기
        count = 0

        for i in range(len(temp)):
            if temp[i] - mid <= 0:
                count += 1
            else:
                count = 0 # 연속으로 0이 나오지 않으면 count 초기화

            if count >= k: # count가 k 이상이 되면 빠져나가기
                break

        if count >= k: 
            right = mid - 1
        else:
            left = mid + 1
    
    return left