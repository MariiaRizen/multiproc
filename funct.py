from multiprocessing import Pool


def collatz(n):
    arr = []
    while n > 1:
        arr.append(n)
        if n % 2:
            n = 3 * n + 1

        else:
            n = n // 2
    return len(arr) + 1


ans = max(range(2, 1000000), key=collatz)


if __name__ == "__main__":
    with Pool(processes=2) as pool:
        result = pool.apply_async(ans, (5,))


    print(result.get())

