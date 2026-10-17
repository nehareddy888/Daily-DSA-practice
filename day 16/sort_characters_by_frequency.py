class Solution:
    def frequencySort(self, s: str) -> str:
        frequencies = {}

        for character in s:
            frequencies[character] = frequencies.get(character, 0) + 1

        characters = list(frequencies)
        size = len(characters)

        for start in range(size):
            most_frequent_index = start

            for index in range(start + 1, size):
                if frequencies[characters[index]] > frequencies[characters[most_frequent_index]]:
                    most_frequent_index = index

            characters[start], characters[most_frequent_index] = characters[most_frequent_index], characters[start]

        result = []
        for character in characters:
            result.append(character * frequencies[character])

        return "".join(result)
