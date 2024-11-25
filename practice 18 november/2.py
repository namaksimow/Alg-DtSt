import time


def c_recursion(n, k):
    if n == 1 and k == 1:
        return 1

    if k == 0:
        return 1

    if n < k:
        return 0

    return c_recursion(n - 1, k - 1) + c_recursion(n - 1, k)


def c_recurrently(n, k):
    if n == 1 and k == 1:
        return 1

    if k == 0:
        return 1

    return c_recurrently(n - 1, k - 1) * n / k


def solve():
    k = int(input("input number K "))
    n = int(input("input number N "))

    start2 = time.time()
    answer2 = c_recurrently(n, k)
    end2 = time.time()
    print(answer2)
    print(f"{end2 - start2} - время нахождения через рекуррентное соотношение")
    start1 = time.time()
    answer1 = c_recursion(n, k)
    end1 = time.time()
    print(answer1)
    print(f"{end1 - start1} - время нахождения через двойную рекурсию")


if __name__ == "__main__":
    solve()