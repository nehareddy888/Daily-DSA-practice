def k_smallest_elements(values: list[int], k: int) -> list[int]:
    result = values[:]

    if k <= 0:
        return []

    if k > len(result):
        k = len(result)

    for start in range(k):
        smallest_index = start

        for index in range(start + 1, len(result)):
            if result[index] < result[smallest_index]:
                smallest_index = index

        result[start], result[smallest_index] = result[smallest_index], result[start]

    return result[:k]
