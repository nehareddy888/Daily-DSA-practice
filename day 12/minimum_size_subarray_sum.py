class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        left = 0
        running_sum = 0
        shortest = float("inf")

        for right, value in enumerate(nums):
            running_sum += value

            while running_sum >= target:
                shortest = min(shortest, right - left + 1)
                running_sum -= nums[left]
                left += 1

        return 0 if shortest == float("inf") else shortest
