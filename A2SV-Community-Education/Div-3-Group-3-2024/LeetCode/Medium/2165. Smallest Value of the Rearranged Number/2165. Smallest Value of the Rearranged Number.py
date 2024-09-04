class Solution:
    def smallestNumber(self, num: int) -> int:
        digits = []
        isneg =  num < 0 
        num = abs(num)
        while num:
            digit = num%10
            digits.append(digit)
            num //= 10
        if isneg:
            digits.sort(reverse=True)
        else:
            digits.sort()
            if len(digits) > 1 and digits[0] == 0:
                l = r = 0 
                while r < len(digits):
                    if digits[r] != 0:
                        digits[l], digits[r] = digits[r], digits[l]
                        break
                    r += 1

        number = 0
        for digit in digits:
            number = number * 10 + digit

        return -number if isneg else number