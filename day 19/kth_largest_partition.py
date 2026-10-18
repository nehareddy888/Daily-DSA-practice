def _partition(values: list[int], low: int, high: int) -> int:
    pivot = values[high]
    boundary = low

    for index in range(low, high):
        if values[index] <= pivot:
            values[boundary], values[index] = values[index], values[boundary]
            boundary += 1

    values[boundary], values[high] = values[high], values[boundary]
    return boundary


def find_kth_largest(nums: list[int], k: int) -> int:
    if k < 1 or k > len(nums):
        raise ValueError("k must be between 1 and the length of nums")

    values = nums[:]
    target = len(values) - k
    low = 0
    high = len(values) - 1

    while low <= high:
        pivot_index = _partition(values, low, high)

        if pivot_index == target:
            return values[pivot_index]
        if pivot_index < target:
            low = pivot_index + 1
        else:
            high = pivot_index - 1

    raise ValueError("k is outside the valid range")
