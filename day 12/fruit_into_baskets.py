class Solution:
    def totalFruit(self, fruits: list[int]) -> int:
        counts = {}
        left = 0
        most_fruit = 0

        for right, fruit in enumerate(fruits):
            counts[fruit] = counts.get(fruit, 0) + 1

            while len(counts) > 2:
                leaving = fruits[left]
                counts[leaving] -= 1
                if counts[leaving] == 0:
                    del counts[leaving]
                left += 1

            most_fruit = max(most_fruit, right - left + 1)

        return most_fruit
