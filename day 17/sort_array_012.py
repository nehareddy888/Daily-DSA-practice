class Solution:
    def sortColors(self, nums: list[int]) -> None:
        for index in range(1, len(nums)):
            current = nums[index]
            position = index - 1

            while position >= 0 and nums[position] > current:
                nums[position + 1] = nums[position]
                position -= 1

            nums[position + 1] = current
