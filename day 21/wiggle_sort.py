class Solution:
    def wiggleSort(self, nums: list[int]) -> None:
        for index in range(len(nums) - 1):
            if index % 2 == 0 and nums[index] > nums[index + 1]:
                nums[index], nums[index + 1] = nums[index + 1], nums[index]
            elif index % 2 == 1 and nums[index] < nums[index + 1]:
                nums[index], nums[index + 1] = nums[index + 1], nums[index]
