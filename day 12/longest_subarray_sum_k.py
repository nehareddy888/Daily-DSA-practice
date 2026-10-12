class Solution:
    def longestSubarray(self, nums: list[int], k: int) -> int:
        left = 0
        running_sum = 0
        longest = 0

        for right, value in enumerate(nums):
            running_sum += value

            while running_sum > k:
                running_sum -= nums[left]
                left += 1

            if running_sum == k:
                longest = max(longest, right - left + 1)

        return longest
