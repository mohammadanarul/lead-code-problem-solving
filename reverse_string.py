class Solution:
    def reverseString(self, s: list[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        left = 0
        right = len(s) - 1
        while left < right:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1
        return s


if __name__ == "__main__":
    items = [["h", "e", "l", "l", "o"], ["H", "a", "n", "n", "a", "h"]]
    for item in items:
        result = Solution().reverseString(item)
