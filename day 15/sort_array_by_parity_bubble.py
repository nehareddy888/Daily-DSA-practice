class Solution:
    def sortArrayByParity(self, nums: list[int]) -> list[int]:
        result = nums[:]
        size = len(result)

        for pass_index in range(size):
            for index in range(0, size - pass_index - 1):
                if result[index] % 2 > result[index + 1] % 2:
                    result[index], result[index + 1] = result[index + 1], result[index]

        return result
