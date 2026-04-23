class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        # Constants
        INT_MAX = 2**31 - 1
        INT_MIN = -2**31
        
        # Overflow case
        if dividend == INT_MIN and divisor == -1:
            return INT_MAX
        
        # Determine sign
        sign = -1 if (dividend < 0) ^ (divisor < 0) else 1
        
        # Work with positive numbers
        dividend = abs(dividend)
        divisor = abs(divisor)
        
        result = 0
        
        # Main logic (bit manipulation)
        while dividend >= divisor:
            temp = divisor
            multiple = 1
            
            # Double until it exceeds dividend
            while dividend >= (temp << 1):
                temp <<= 1
                multiple <<= 1
            
            dividend -= temp
            result += multiple
        
        return sign * result