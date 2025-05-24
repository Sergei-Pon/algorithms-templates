from typing import List, Tuple


def moving_average(n: int, arr: List[int], window: int) -> List[float]:
    x = sum(arr[0:window])
    result = [x / window]
    for i in range(n - window):
        x -= arr[i]
        x += arr[i + window]
        result.append(x / window)
    return result


def read_input() -> Tuple[int, List[int], int]:
    with open('input.txt', 'r') as file_in:
        n = int(file_in.readline())
        arr = list(map(int, file_in.readline().strip().split()))
        window = int(file_in.readline())
    return n, arr, window


def main():
    n, arr, window = read_input()
    print(" ".join(map(str, moving_average(n, arr, window))))


if __name__ == '__main__':
    main()
