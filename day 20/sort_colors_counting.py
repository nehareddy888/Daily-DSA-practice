class Solution:
    def sortColors(self, nums: list[int]) -> None:
        counts = [0, 0, 0]

        for value in nums:
            counts[value] += 1

        position = 0
        for value in range(3):
            for _ in range(counts[value]):
                nums[position] = value
                position += 1
