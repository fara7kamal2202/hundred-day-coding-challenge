from random import randint
import numpy as np

def get_password(num_letters: int, num_digits: int, num_symbols: int) -> str:

    symbol_ascii_range = (33, 47)
    letter_ascii_range = [(65, 90), (97, 122)]
    password_char = []
    password = ""

    for i in range(num_letters):
        case = letter_ascii_range[randint(0, 1)]
        password_char.append(chr(randint(case[0], case[1])))
    for i in range(num_digits):
        password_char.append(str(randint(0, 9)))
    for i in range(num_symbols):
        password_char.append(chr(randint(symbol_ascii_range[0], symbol_ascii_range[1])))

    np.random.shuffle(password_char)
    password = "".join(password_char)

    return password


random_password = get_password(5, 6, 3)
print(random_password)

