import re


class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        if not s:
            return 0
        text = re.sub(r"\s+", " ", s.strip()).strip()
        return len(text.split()[-1]) if text else 0


if __name__ == "__main__":
    items = [
        "Hello World",
        "Python Programming",
        "OpenAI GPT",
        "Code Review",
        "Length of Last Word",
        "Test Cases",
        "SingleWord",
        "Trailing Spaces   ",
        "   Leading Spaces",
        "   ",
        "NoSpaces",
        "   Multiple   Spaces   ",
    ]
    for sentence in items:
        result = Solution().lengthOfLastWord(sentence)
        print(f"Length of the last word: {result}")
