class ParenthesesValidator:
    def is_valid(self, s):
        stack = []
        mapping = {')': '(', '}': '{', ']': '['}
        for char in s:
            if char in mapping:
                top = stack.pop() if stack else '#'
                if mapping[char] != top:
                    return False
            else:
                stack.append(char)
        return not stack

validator = ParenthesesValidator()
s = input("Enter a string of parentheses: ")
print(validator.is_valid(s))
