def merge_sorted_arrays(first: list[int], second: list[int]) -> list[int]:
    merged = []
    first_index = 0
    second_index = 0

    while first_index < len(first) and second_index < len(second):
        if first[first_index] <= second[second_index]:
            merged.append(first[first_index])
            first_index += 1
        else:
            merged.append(second[second_index])
            second_index += 1

    while first_index < len(first):
        merged.append(first[first_index])
        first_index += 1

    while second_index < len(second):
        merged.append(second[second_index])
        second_index += 1

    return merged
