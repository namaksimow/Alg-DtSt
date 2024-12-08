import random


def create_matrix(count_project, max_sum_investment):
    min_sum = 0
    low_border = 2
    high_border = 8
    count_row = max_sum_investment // 10 + 1
    count_column = count_project + 1
    matrix = [[0 for _ in range(count_column)] for _ in range(count_row)]
    profit_matrix = [[0 for _ in range(count_column)] for _ in range(count_row)]
    for i in range(0, count_row):
        matrix[i][0] = min_sum
        profit_matrix[i][0] = min_sum
        min_sum += 10

    for i in range(1, count_row):
        for j in range(1, count_column):
            matrix[i][j] = random.randint(low_border, high_border)
        low_border += 10
        high_border += 10
    print("\ntable of start matrix")
    for row in matrix:
        print(" | ".join(f"{num:3d}" for num in row))
    print("\ntable of max profit")
    return matrix, profit_matrix


def fill_profit_matrix(matrix, profit_matrix, count_project, max_sum_investment):
    count_row = max_sum_investment // 10 + 1
    count_column = count_project + 1

    for i in range(1, count_column):
        for j in range(1, count_row):

            if i == 1:
                profit_matrix[j][i] = matrix[j][i]
            else:
                max_variants = []
                left_column_index = 0
                right_column_index = j
                for k in range(j + 1):
                    variant = profit_matrix[left_column_index][i - 1] + matrix[right_column_index][i]
                    max_variants.append(variant)
                    left_column_index += 1
                    right_column_index -= 1

                profit_matrix[j][i] = max(max_variants)

    for row in profit_matrix:
        print(" | ".join(f"{num:3d}" for num in row))

    print(profit_matrix[-1][-1])


def solve():
    count_project = int(input("Input count projects: "))
    max_sum_investment = int(input("Input max sum of investments: "))
    matrix, profit_matrix = create_matrix(count_project, max_sum_investment)
    fill_profit_matrix(matrix, profit_matrix, count_project, max_sum_investment)


if __name__ == "__main__":
    solve()
