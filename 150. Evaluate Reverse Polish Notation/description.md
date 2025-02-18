### 150. Evaluate Reverse Polish Notation

You are given an array of strings `tokens` that represents a valid arithmetic expression in **Reverse Polish Notation**.

Evaluate the expression and return an integer that represents the result.

**Note:**
- The valid operators are `'+'`, `'-'`, `'*'`, and `'/'`.
- Each operand may be an integer or another expression.
- Division between two integers truncates toward zero.
- The given expression is always valid and will evaluate to a single integer.

#### Example 1:
**Input:** `tokens = ["2","1","+","3","*"]`
**Output:** `9`
**Explanation:** `((2 + 1) * 3) = 9`

#### Example 2:
**Input:** `tokens = ["4","13","5","/","+"]`
**Output:** `6`
**Explanation:** `(4 + (13 / 5)) = 6`

#### Example 3:
**Input:** `tokens = ["10","6","9","3","/","-11","*","+","*","17","+","5","+"]`
**Output:** `22`

#### Constraints:
- `1 <= tokens.length <= 10^4`
- `tokens[i]` is either an operator (`"+", "-", "*", "/"`) or an integer in the range `[-200, 200]`.