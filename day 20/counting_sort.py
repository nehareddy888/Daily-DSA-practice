def counting_sort(values: list[int]) -> list[int]:
    if not values:
        return []

    smallest = values[0]
    largest = values[0]

    for value in values[1:]:
        if value < smallest:
            smallest = value
        if value > largest:
            largest = value

    counts = [0] * (largest - smallest + 1)

    for value in values:
        counts[value - smallest] += 1

    result = []
    for offset in range(len(counts)):
        for _ in range(counts[offset]):
            result.append(offset + smallest)

    return result
