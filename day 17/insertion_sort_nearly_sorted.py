def sort_nearly_sorted(values: list[int]) -> list[int]:
    result = values[:]

    for index in range(1, len(result)):
        current = result[index]
        position = index - 1

        while position >= 0 and result[position] > current:
            result[position + 1] = result[position]
            position -= 1

        result[position + 1] = current

    return result
