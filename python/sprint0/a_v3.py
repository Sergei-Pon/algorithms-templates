# a.py

from typing import Tuple


def get_sum(a: int, b: int) -> int:
    return a + b


def read_input() -> Tuple[int, int]:
    with open('input.txt', 'r') as file_in:
        a = int(file_in.readline())
        b = int(file_in.readline())
    return a, b


def main():
    a, b = read_input()
    # print(get_sum(a, b))
    with open('output.txt', 'w') as file_out:
        file_out.write(str(get_sum(a, b)))


if __name__ == '__main__':
    main()
