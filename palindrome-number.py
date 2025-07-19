class Solution:
    def isPalindrome(self, x: int) -> bool:
        if not x:
            return False
        return str(x) == str(x)[::-1]


if __name__ == "__main__":
    items = [
        121,
        -121,
        10,
        12321,
        "madam",
        "racecar",
        "radar",
        "civic",
        "rotor",
        "level",
    ]
    for item in items:
        result = Solution().isPalindrome(item)
        print(f"Is {item} a palindrome? {result}")
