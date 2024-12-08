import time


def two_dimension_matrix(number_k, number_n):
    matrix = [[0 for x in range(number_n + 1)] for y in range(number_n + 1)]
    matrix[0][0] = 1

    for i in range(1, number_n + 1):
        for j in range(i + 1):
            matrix[i][j] = matrix[i - 1][j - 1] + matrix[i - 1][j]

    return matrix[number_n][number_k]


def one_dimensional_matrix(number_k, number_n):
    number_to_array = number_n + 1
    array_length = int((number_to_array + 1) / 2 * number_to_array)
    start_index = 1
    end_index = 2
    matrix = [0 for n in range(array_length)]
    matrix[0] = 1
    for i in range(1, number_n + 1):
        for j in range(i + 1):
            if j == 0 or j == i:
                matrix[start_index + j] = 1
            else:
                matrix[start_index + j] = matrix[start_index + j - i] + matrix[start_index + j - i - 1]
        start_index = end_index + 1
        end_index = end_index + i + 2

    return matrix[array_length - number_k - 1]


def solve():
    k = int(input("input number K "))
    n = int(input("input number N "))
    start1 = time.time()
    answer1 = two_dimension_matrix(k, n)
    end1 = time.time()
    print(answer1)
    print(f"{end1 - start1} - время нахождения в двумерной матрице")
    start2 = time.time()
    answer2 = one_dimensional_matrix(k, n)
    end2 = time.time()
    print(answer2)
    print(f"{end2 - start2} - время выполнения в одномерном массиве")


if __name__ == "__main__":
    solve()