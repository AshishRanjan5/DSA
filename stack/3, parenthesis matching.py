"""
Given a string s, composed of different combinations of '(' , ')', '{', '}', '[', ']'. Determine whether the Expression is balanced or not.
An expression is balanced if:

Each opening bracket has a corresponding closing bracket of the same type.
Opening brackets must be closed in the correct order.
Examples :

Input: s = "[{()}]"
Output: true
Explanation: All the brackets are well-formed.
Input: s = "[()()]{}"
Output: true
Explanation: All the brackets are well-formed.
Input: s = "([]"
Output: false
Explanation: The expression is not balanced as there is a missing ')' at the end.
Input: s = "([{]})"
Output: false
Explanation: The expression is not balanced as there is a closing ']' before the closing '}'.
"""

class Expression:
    def isBalanced(self, s):
        stack = []
        for ch in s:
            if ch == "(" or ch == "{" or ch == "[":
                stack.append(ch)
            
            if ch == ")":
                if not stack or stack[-1] != "(":
                    return False
                stack.pop()
            
            if ch == "}":
                if not stack or stack[-1] != "{":
                    return False
                stack.pop()
            
            if ch == "]":
                if not stack or stack[-1] != "[":
                    return False
                stack.pop()
        
        if len(stack) == 0:
            return True


if __name__ == "__main__":
    s1 = "[{()}]"
    s2 = "[()()]{}"
    s3 = "([{]})"

    exp = Expression()
    print(exp.isBalanced(s3)) 