def bubble_sort(values: list[int]) -> list[int]:
    result = values[:]
    size = len(result)

    for pass_index in range(size):
        swapped = False

        for index in range(0, size - pass_index - 1):
            if result[index] > result[index + 1]:
                result[index], result[index + 1] = result[index + 1], result[index]
                swapped = True

        if not swapped:
            break

    return result
