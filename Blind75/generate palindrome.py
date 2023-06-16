def GPalindrome(n):

    stack = []
    res = []    

    def backtracking(open, close):

        if open == close == n:
            res.append("".join(stack))
            return

        if open < n:
            stack.append("(")
            backtracking(open+1, close)
            stack.pop()

        if close < open:
            stack .append(")")
            backtracking(open, close+1)
            stack.pop()

    backtracking(0, 0)
    return res


n = 3
print(GPalindrome(n))
