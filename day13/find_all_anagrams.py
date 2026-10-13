class Solution:
    def findAnagrams(self, s: str, p: str) -> list[int]:
        window_size = len(p)
        if window_size > len(s):
            return []

        needed = {}
        for character in p:
            needed[character] = needed.get(character, 0) + 1

        present = {}
        satisfied = 0
        required = len(needed)
        starts = []
        left = 0

        for right, character in enumerate(s):
            present[character] = present.get(character, 0) + 1
            if character in needed:
                if present[character] == needed[character]:
                    satisfied += 1
                elif present[character] == needed[character] + 1:
                    satisfied -= 1

            if right - left + 1 > window_size:
                leaving = s[left]
                if leaving in needed:
                    if present[leaving] == needed[leaving]:
                        satisfied -= 1
                    elif present[leaving] == needed[leaving] + 1:
                        satisfied += 1
                present[leaving] -= 1
                if present[leaving] == 0:
                    del present[leaving]
                left += 1

            if right - left + 1 == window_size and satisfied == required:
                starts.append(left)

        return starts
