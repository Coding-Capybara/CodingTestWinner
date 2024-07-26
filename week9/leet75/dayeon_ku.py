# 솔루션에 있는 O(n) 코드
# Dutch Partitioning Problem이라고 함
# def sortColors(self, nums):
#     red, white, blue = 0, 0, len(nums)-1
    
#     while white <= blue:
#         if nums[white] == 0:
#             nums[red], nums[white] = nums[white], nums[red]
#             white += 1
#             red += 1
#         elif nums[white] == 1:
#             white += 1
#         else:
#             nums[white], nums[blue] = nums[blue], nums[white]
#             blue -= 1
            
            
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        nums.sort()