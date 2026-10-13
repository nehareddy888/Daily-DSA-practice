class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        window_size = len(s1)
        if window_size > len(s2):
            return False
        if window_size == 0:
            return True

        needed = {}
        for character in s1:
            needed[character] = needed.get(character, 0) + 1

        present = {}
        satisfied = 0
        required = len(needed)
        left = 0

        for right, character in enumerate(s2):
            present[character] = present.get(character, 0) + 1
            if character in needed:
                if present[character] == needed[character]:
                    satisfied += 1
                elif present[character] == needed[character] + 1:
                    satisfied -= 1

            if right - left + 1 > window_size:
                leaving = s2[left]
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
                return True

        return False
