### 11. Container With Most Water

You are given an integer array `height` of length `n`. There are `n` vertical lines drawn such that the two endpoints of the `i`th line are `(i, 0)` and `(i, height[i])`.

Find two lines that together with the x-axis form a container, such that the container contains the most water.

Return the **maximum amount of water** a container can store.

**Note:** You may not slant the container.

#### Example 1:
**Input:** `height = [1,8,6,2,5,4,8,3,7]`
**Output:** `49`
**Explanation:** The above vertical lines are represented by an array `[1,8,6,2,5,4,8,3,7]`. The maximum area is between lines at index `1` and `8`, forming a container of height `7` and width `7`, storing `49` units of water.

#### Example 2:
**Input:** `height = [1,1]`
**Output:** `1`

#### Constraints:
- `2 <= height.length <= 10^5`
- `0 <= height[i] <= 10^4`