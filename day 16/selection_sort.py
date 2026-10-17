def selection_sort(values: list[int]) -> list[int]:
    result = values[:]
    size = len(result)

    for start in range(size):
        smallest_index = start

        for index in range(start + 1, size):
            if result[index] < result[smallest_index]:
                smallest_index = index

        result[start], result[smallest_index] = result[smallest_index], result[start]

    return result
