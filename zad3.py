def is_even(digit: int) -> bool:
    return digit%2 == 0

result = is_even(4)

if result:
    print("Liczba parzysta!")
else:
    print("Liczba nieparzysta!")