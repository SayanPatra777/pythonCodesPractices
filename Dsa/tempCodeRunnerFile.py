def bubbleSort(nums:list[int])->list[int]:
#     lenNums=len(nums)
#     for i in range (lenNums):
#         isSwap=False
#         for j in range (lenNums-i-1):
#             if nums[j]>nums[j+1]:
#                 nums[j],nums[j+1]=nums[j+1],nums[j]
#                 isSwap=True
#         if not isSwap:
#             break
#     return nums

# if __name__ == "__main__":
#     nums = list(map(int, input("Enter the Numbers in the array separated with space :\n").split()))
#     print(bubbleSort(nums))