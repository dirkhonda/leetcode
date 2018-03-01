def plusOne(self, digits):
    length = len(digits)
    i = length-1
    remainder = 1

    while (i + 1) > 0:
        value = digits[i] + remainder
        digits[i] = value % 10
        remainder = value // 10
        i -= 1
    if remainder:
        digits.insert(0, remainder)
    return digits


plusOne(None, [8, 9, 9, 9])

