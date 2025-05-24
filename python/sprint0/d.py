from typing import List, Tuple, Optional


def two_sum(arr: List[int], target_sum: int) -> Optional[Tuple[int, int]]:
    a = set(arr)
    b = list(a)
    for i in range(len(a)):
        for j in range(len(a)):
            if (b[i] + b[j] == target_sum) and (b[i] != b[j]):
                return b[i], b[j]
    return None


def read_input() -> Tuple[List[int], int]:
    with open('input.txt', 'r') as file_in:
        n = int(file_in.readline())
        arr = list(map(int, file_in.readline().strip().split()))
        target_sum = int(file_in.readline())
    return arr, target_sum


def print_result(result: Optional[Tuple[int, int]]) -> None:
    if result is None:
        print(None)
    else:
        print(" ".join(map(str, result)))


def main():
    arr, target_sum = read_input()
    print_result(two_sum(arr, target_sum))


if __name__ == '__main__':
    main()
