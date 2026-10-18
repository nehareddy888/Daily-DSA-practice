class Solution:
    def frequencySort(self, nums: list[int]) -> list[int]:
        frequencies = {}

        for value in nums:
            frequencies[value] = frequencies.get(value, 0) + 1

        values = list(frequencies)

        for index in range(1, len(values)):
            current = values[index]
            position = index - 1

            while position >= 0 and (
                frequencies[current] < frequencies[values[position]]
                or (
                    frequencies[current] == frequencies[values[position]]
                    and current > values[position]
                )
            ):
                values[position + 1] = values[position]
                position -= 1

            values[position + 1] = current

        result = []
        for value in values:
            for _ in range(frequencies[value]):
                result.append(value)

        return result
