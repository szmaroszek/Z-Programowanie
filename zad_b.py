def modify_digits(digits):
    for i, digit in enumerate(digits):
        digits[i] = digits[i] * 2
    return digits

def modify_digits_2(digits):
    return [digit * 2 for digit in digits]

digits = [1, 2, 3, 4, 5]

new_digits_2 = modify_digits_2(digits)
new_digits = modify_digits(digits)

print(new_digits)
print(new_digits_2)