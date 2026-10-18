def _sort_and_count(values: list[int]) -> tuple[list[int], int]:
    if len(values) <= 1:
        return values[:], 0

    middle = len(values) // 2
    left, left_inversions = _sort_and_count(values[:middle])
    right, right_inversions = _sort_and_count(values[middle:])

    merged = []
    left_index = 0
    right_index = 0
    split_inversions = 0

    while left_index < len(left) and right_index < len(right):
        if left[left_index] <= right[right_index]:
            merged.append(left[left_index])
            left_index += 1
        else:
            merged.append(right[right_index])
            right_index += 1
            split_inversions += len(left) - left_index

    while left_index < len(left):
        merged.append(left[left_index])
        left_index += 1

    while right_index < len(right):
        merged.append(right[right_index])
        right_index += 1

    return merged, left_inversions + right_inversions + split_inversions


def count_inversions(values: list[int]) -> int:
    _, inversions = _sort_and_count(values)
    return inversions
