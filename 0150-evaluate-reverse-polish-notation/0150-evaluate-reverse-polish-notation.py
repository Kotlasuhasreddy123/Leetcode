class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        stack = []
        opera = ["+", "-", "*", "/"]

        for i in tokens:
            if i not in opera:
                stack.append(int(i))
            else:
                r = stack.pop()
                l = stack.pop()
            if i == "+":
                stack.append(l + r)
            elif i == "-":
                stack.append(l - r)
            elif i == "*":
                stack.append(l * r)
            elif i == "/":
                stack.append(int(l / r))
        return stack[0]
