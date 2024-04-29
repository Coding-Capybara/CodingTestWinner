def solution(stones, k):
    answer = 0
    
    left, right = 0, max(stones)
    
    while left <= right:
        mid = (left + right) // 2
        cnt = 0
        for stone in stones:
            if stone < mid:
                cnt += 1
            else:
                cnt = 0
                
            if cnt == k:
                break
        
        if cnt < k:
            answer = mid
            left = mid + 1
        else:
            right = mid - 1
        
            
    return answer

# ========================================================= #  
## 2번
# import numpy as np

# def solution(stones, k):
#     answer = 0
#     chk = True
    
#     stones = np.array(stones)
                
#     while chk:
#         for i in range(0, len(stones)):
#             templst = stones[i:i+k]
#             if np.sum(templst) == 0 and len(templst) == k:
#                 chk = False
#                 break
#         if chk:
#             answer += 1
#             stones = np.maximum(0, stones - 1)
#         else:
#             break
            
#     return answer


# ========================================================= #  
## 1번
# import numpy as np

# def solution(stones, k):
#     answer = 0
#     cnt = 0
    
#     stones = np.array(stones)
                
#     while cnt < k:
#         cnt = 0
        
#         for i in range(len(stones)):
#             if stones[i] == 0:
#                 cnt += 1
#             else:
#                 cnt = 0
                
#             if cnt >= k:
#                 break
                
#         if cnt >= k:
#             break
#         else:
#             stones = np.maximum(0, stones - 1)
#             answer += 1

#     return answer
