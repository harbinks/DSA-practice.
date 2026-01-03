class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        mapping = {')': '(', ']': '[', '}': '{'}

        for ch in s:
            if ch in mapping:
                if not stack or stack[-1] != mapping[ch]:
                    return False
                stack.pop()
            else:
                stack.append(ch)

        return not stack

if __name__ == "__main__":
    sol = Solution()
    tests = ["()", "()[]{}", "(]", "([)]", "{[]}", "((("]
    for t in tests:
        print(t, "->", sol.isValid(t))

