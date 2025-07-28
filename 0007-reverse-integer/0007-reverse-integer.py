class Solution:
    def reverse(self, x: int) -> int:
        dup = abs(x)
        result = 0

        while dup != 0:
            d = dup % 10
            if result > (2**31 - 1) // 10 or (result == (2**31 - 1) // 10 and d > 7):
                return 0
            result = result * 10 + d
            dup = dup // 10

        if x < 0:
            result *= -1

        if -2**31 <= result <= (2**31 - 1):
            return result
        else:
            return 0
