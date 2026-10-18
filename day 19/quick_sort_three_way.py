def _quick_sort(values: list[int], low: int, high: int) -> None:
    if low >= high:
        return

    pivot = values[(low + high) // 2]
    less = low
    current = low
    greater = high

    while current <= greater:
        if values[current] < pivot:
            values[less], values[current] = values[current], values[less]
            less += 1
            current += 1
        elif values[current] > pivot:
            values[current], values[greater] = values[greater], values[current]
            greater -= 1
        else:
            current += 1

    _quick_sort(values, low, less - 1)
    _quick_sort(values, greater + 1, high)


def quick_sort_three_way(values: list[int]) -> list[int]:
    result = values[:]
    _quick_sort(result, 0, len(result) - 1)
    return result
