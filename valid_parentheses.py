class Solution:
    def isValid(self, s: str) -> bool:
        if s is None or len(s) == 0:
            return False
        stk = []
        mapping = {")": "(", "]": "[", "}": "{"}
        for ch in s:
            if ch in "({[":
                stk.append(ch)
            else:
                if len(stk) == 0:
                    return False
                last_ch = stk.pop()
                if ch in mapping:
                    if mapping[ch] != last_ch:
                        return False
        return stk == []


if __name__ == "__main__":
    strings = [
        "()",
        "()[]{}",
        "(]",
        "([)]",
        "{[]}",
        "((()))",
        "((())",
        "((())())",
        "",
    ]
    for s in strings:
        result = Solution().isValid(s)
        print(f"The string '{s}' is valid: {result}")
