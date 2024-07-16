class Solution:
    def countDigitOne(self, n: int) -> int:
        count, factor, lower = 0, 1, 0
        while n > 0:
            digit = n % 10
            higher = n // 10
            if digit == 0:
                count += higher * factor
            elif digit == 1:
                count += higher * factor + lower + 1
            else:
                count += (higher + 1) * factor
            lower += digit * factor
            factor *= 10
            n //= 10
        return count
