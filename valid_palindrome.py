class Solution:
    def isPalindrome(self, s: str) -> bool:
        filtered_chars = "".join(c.lower() for c in s if c.isalnum())
        return filtered_chars == filtered_chars[::-1]


if __name__ == "__main__":
    items = [
        "A man, a plan, a canal: Panama",
        "race a car",
        " ",
    ]
    for item in items:
        result = Solution().isPalindrome(item)
        print(f"Is the string '{item}' a palindrome? {result}")
