# Day 12 — Variable-Size Sliding Window

Today’s three problems all use the same useful idea: keep a window over a stretch of the array, and move its edges as the answer changes. The window grows to include new values. When it stops being valid, move the left edge forward until it is valid again.

The important detail is that each solution updates a running total or count as the window moves. It never makes a fresh slice and sums it again.

## 1. Minimum Size Subarray Sum

**File:** [minimum_size_subarray_sum.py](minimum_size_subarray_sum.py)

We want the shortest continuous run of numbers whose sum reaches the target. As we move across the list, we add each new number to the running total. Whenever the total is large enough, we have a valid run, so we record its length and keep moving the left edge forward. That checks whether dropping numbers from the front can give us an even shorter run. If no run reaches the target, the answer is `0`.

This sliding-window approach assumes the numbers are positive, as in the standard version of the problem. Positivity matters: removing a number from the left can only make the sum smaller, so the window can be adjusted in a predictable way.

## 2. Longest Subarray with Sum K

**File:** [longest_subarray_sum_k.py](longest_subarray_sum_k.py)

Here we want the longest continuous run whose sum is exactly `k`. We grow the window by adding numbers on the right. If its sum goes past `k`, we remove numbers from the left until it is back within range. Whenever the sum equals `k`, we compare this run’s length with the best one seen so far.

This version also expects positive numbers. With positive numbers, a sum that is too large can be reduced by moving the left edge; that reasoning would not hold for arrays containing negative numbers.

## 3. Fruit Into Baskets

**File:** [fruit_into_baskets.py](fruit_into_baskets.py)

Each fruit type is represented by a number, and the two baskets can hold at most two types. We keep a window and count the types inside it. When a third type appears, we move the left edge forward and update the counts until only two types remain. The largest valid window we find is the most fruit we can pick in one continuous stretch.

## Complexity

Each solution takes **O(n)** time: every value enters the window once and leaves it at most once. The first two use **O(1)** extra space, and the basket solution uses **O(1)** extra space because it tracks at most three fruit types at a time while shrinking.
