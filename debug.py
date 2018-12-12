def main():
    for _ in range(int(input())):
        n, lb, ub = map(int, input().split())
        array = list(map(int, input().split()))
        count = 0
        for i in range(1, 2 ** n):
            total = 0
            for j in range(n):
                if i & (1 << j):
                    total += array[j]
            if lb <= total <= ub:
                count += 1
        print(count)


if __name__ == '__main__':
    main()