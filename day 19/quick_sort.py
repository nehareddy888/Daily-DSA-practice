def _lomuto_partition(values: list[int], low: int, high: int) -> int:
    pivot = values[high]
    boundary = low

    for index in range(low, high):
        if values[index] <= pivot:
            values[boundary], values[index] = values[index], values[boundary]
            boundary += 1

    values[boundary], values[high] = values[high], values[boundary]
    return boundary


def _quick_sort_lomuto(values: list[int], low: int, high: int) -> None:
    if low < high:
        pivot_index = _lomuto_partition(values, low, high)
        _quick_sort_lomuto(values, low, pivot_index - 1)
        _quick_sort_lomuto(values, pivot_index + 1, high)


def quick_sort_lomuto(values: list[int]) -> list[int]:
    result = values[:]
    _quick_sort_lomuto(result, 0, len(result) - 1)
    return result


def _hoare_partition(values: list[int], low: int, high: int) -> int:
    pivot = values[(low + high) // 2]
    left = low - 1
    right = high + 1

    while True:
        left += 1
        while values[left] < pivot:
            left += 1

        right -= 1
        while values[right] > pivot:
            right -= 1

        if left >= right:
            return right

        values[left], values[right] = values[right], values[left]


def _quick_sort_hoare(values: list[int], low: int, high: int) -> None:
    if low < high:
        split = _hoare_partition(values, low, high)
        _quick_sort_hoare(values, low, split)
        _quick_sort_hoare(values, split + 1, high)


def quick_sort_hoare(values: list[int]) -> list[int]:
    result = values[:]
    _quick_sort_hoare(result, 0, len(result) - 1)
    return result
