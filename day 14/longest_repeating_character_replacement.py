class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        counts = {}
        left = 0
        max_frequency = 0
        longest = 0

        for right, character in enumerate(s):
            counts[character] = counts.get(character, 0) + 1
            max_frequency = max(max_frequency, counts[character])

            while right - left + 1 - max_frequency > k:
                leaving = s[left]
                counts[leaving] -= 1
                left += 1

            longest = max(longest, right - left + 1)

        return longest
