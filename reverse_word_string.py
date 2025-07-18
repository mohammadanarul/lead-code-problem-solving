import re


class Solution:
    def reverseWords(self, s: str) -> str:
        s = re.sub(r"\s+", " ", s).strip()
        result = s.split()
        return " ".join(result[::-1])


if __name__ == "__main__":
    items = ["the sky is blue", "  hello world  ", "a good example"]
    for item in items:
        result = Solution().reverseWords(item)
        print(f"Input: '{item}' => Output: '{result}'")
