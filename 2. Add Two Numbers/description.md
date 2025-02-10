# 2. Add Two Numbers

## Problem Statement
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in **reverse order**, and each node contains a single digit. Your task is to add the two numbers and return their sum as a linked list in the same reverse order format.

**Note**: 
- The numbers do not contain leading zeros, except for the number `0` itself.
- The linked lists are guaranteed to represent valid non-negative integers.

## Examples
### Example 1
- **Input**:  
  `l1 = [2,4,3]` (represents the number 342)  
  `l2 = [5,6,4]` (represents the number 465)  
- **Output**: `[7,0,8]` (represents the number 807)  
- **Explanation**:  
  `342 + 465 = 807`, which is stored in reverse order as `7 -> 0 -> 8`.

### Example 2
- **Input**:  
  `l1 = [0]`, `l2 = [0]`  
- **Output**: `[0]`  

### Example 3
- **Input**:  
  `l1 = [9,9,9,9,9,9,9]` (represents 9999999)  
  `l2 = [9,9,9,9]` (represents 9999)  
- **Output**: `[8,9,9,9,0,0,0,1]` (represents 10009998)  

## Constraints
- The number of nodes in each linked list is between `1` and `100`.
- `0 <= Node.val <= 9`.
- The input lists represent numbers without leading zeros (except for the number `0`).

## Solution Strategy (High-Level)
The goal is to traverse both linked lists simultaneously, summing corresponding digits while managing any carry generated. The result is constructed digit-by-digit in a new linked list. Key steps include:
1. Iterating through both lists until all nodes and any remaining carry are processed.
2. Calculating the sum of current digits and carry.
3. Appending the resulting digit to the answer list.
4. Updating the carry for the next iteration.

This approach ensures an efficient solution with linear time complexity relative to the input size.