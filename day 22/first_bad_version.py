class Solution:
    def firstBadVersion(self, n: int) -> int:
        low = 1
        high = n

        while low < high:
            middle = low + (high - low) // 2

            if isBadVersion(middle):
                high = middle
            else:
                low = middle + 1

        return low
