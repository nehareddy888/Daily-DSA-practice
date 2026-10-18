def sort_binary_array(values: list[int]) -> list[int]:
    result = values[:]
    zero_count = 0

    for value in result:
        if value == 0:
            zero_count += 1

    for index in range(len(result)):
        if index < zero_count:
            result[index] = 0
        else:
            result[index] = 1

    return result
