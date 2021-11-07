def get_elements(digits):
    for i in range(len(digits)):
        if (i % 2 != 0):
            print(digits[i])

digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

get_elements(digits)