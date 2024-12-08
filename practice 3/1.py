import math


def solve_formula(number_n):
    first_slag = (3 - 3**0.5) / 12
    second_slag = (1 - 3**0.5) ** number_n
    third_slag = (3 + 3**0.5) / 12
    fourth_slag = (1 + 3**0.5) ** number_n
    a_n = math.ceil(first_slag * second_slag + third_slag * fourth_slag)
    print(a_n)


def recursion_a(number_n):
    if number_n == 0:
        return 1

    if number_n == 1:
        return recursion_a(number_n - 1)

    return recursion_a(number_n - 1) + recursion_b(number_n - 1) + recursion_c(number_n - 1)


def recursion_b(number_n):
    if number_n == 1:
        return 1

    return recursion_a(number_n - 1) + recursion_b(number_n - 1) + recursion_c(number_n - 1)


def recursion_c(number_n):
    if number_n == 1:
        return 1

    return recursion_a(number_n - 1) + recursion_b(number_n - 1)


if __name__ == "__main__":
    n = int(input("input number N "))
    record = []
    print(f"{solve_formula(n)} - ответ для формулы")
    answer = recursion_a(n)
    print(f"{answer} - ответ для тройной рекурсии")