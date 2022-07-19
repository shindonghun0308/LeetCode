# class Solution:
#     def runningSum(self, nums: List[int]) -> List[int]:
#         output = nums.copy()
#         i = len(nums) - 1
#         while i >=0:
#             output[i] = sum(nums[:i+1])
#             i -= 1
#         return output

class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        output = []
        i = 0
        value = 0
        while i <= len(nums) - 1:
            value += nums[i]
            output.append(value)
            i += 1
        return output
