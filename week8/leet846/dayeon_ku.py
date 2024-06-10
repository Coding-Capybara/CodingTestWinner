# heap 사용한 코드
# hand = [2,1,2,4,1,3,3,3]
# groupSize = 2
# 위 테케에서 막힘
# import heapq

# class Solution:
#     def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
#         if len(hand) % groupSize != 0:
#             return False
        
#         heapq.heapify(hand)

#         ans = True
#         temp = []
#         dummy = []
#         while hand:
#             if len(temp) == groupSize:
#                 temp = []
#                 if dummy:
#                     for i in dummy:
#                         heapq.heappush(hand, i)
#                     dummy = []

#             curr = heapq.heappop(hand)

#             if not temp:
#                 temp.append(curr)
#             else:
#                 if temp[-1] == curr:
#                     if temp[-1] + 1 in hand:
#                         dummy.append(curr)
#                     else:
#                         ans = False
#                         break
#                 elif temp[-1] + 1 == curr:
#                     temp.append(curr)
#                 else:
#                     ans = False
#                     break

#         if len(temp) < groupSize:
#             ans = False

#         return ans

class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False
        
        ans = True
        temp = []
        while hand:
            if len(temp) == groupSize:
                temp = []

            hand.sort()

            if not temp:
                temp.append(hand.pop(0))
            else:
                if temp[-1] + 1 in hand:
                    nxt = temp[-1] + 1
                    temp.append(nxt)
                    hand.remove(nxt)
                else:
                    ans = False
                    break

        return ans