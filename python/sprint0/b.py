def main():
    with open('input.txt', 'r') as file_in:
        n = int(file_in.readline())
        a = list(file_in.readline().split())
        b = list(file_in.readline().split())
    result = []
    for i in range(n):
        result.append(a[i])
        result.append(b[i])
    print(" ".join(result))


if __name__ == '__main__':
    main()
