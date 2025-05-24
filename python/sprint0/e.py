from typing import List, Tuple, Optional


def two_sum(arr: List[int], target_sum: int) -> Optional[Tuple[int, int]]:
    b = arr
    for i in range(len(b)):
        if (b[i] + abs(b[0])) > (target_sum + abs(b[0])):
            break
        for j in range(len(b)):
            if i == j:
                continue
            print(b[i] + b[j])
            if (b[i] + b[j] == target_sum):
                return b[i], b[j]
            elif (b[i] + b[j] > target_sum):
                break
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
