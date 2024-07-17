# Define integer limit constants
INT_MAX = 2**31 - 1
INT_MIN = -2**31

class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        # Set negative variable
        negative = (dividend >= 0) ^ (divisor >= 0)
        dividend = abs(dividend)
        divisor = abs(divisor)

        # Set variables and align bit position difference
        quotient = 0
        temp_divisor = divisor
        bit_position = dividend.bit_length() - divisor.bit_length()

        # Perform the division
        while bit_position >= 0:
            if (temp_divisor << bit_position) <= dividend:
                quotient += 1 << bit_position
                dividend -= temp_divisor << bit_position
            bit_position -= 1

        # Apply negative
        if negative:
            quotient = 0 - quotient
        
        # Constrain quotient to integer limits
        if quotient > INT_MAX:
            quotient = INT_MAX
        elif quotient < INT_MIN:
            quotient = INT_MIN

        return quotient
