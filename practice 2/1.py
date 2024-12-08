def recursion_add_one(current_string, number_length, array_to_record):
    return recursion(current_string + "1", number_length, array_to_record)


def recursion_add_zero(current_string, number_length, array_to_record):
    return recursion(current_string + "0", number_length, array_to_record)


def recursion(current_string, number_length, array_to_record):
    if len(current_string) == number_length:
        array_to_record.append(current_string)
        return

    if len(current_string) == 0:
        recursion_add_one(current_string, number_length, array_to_record)
        recursion_add_zero(current_string, number_length, array_to_record)
    else:
        if current_string[-1] == "0":
            recursion_add_one(current_string, number_length, array_to_record)

        if current_string[-1] == "1":
            recursion_add_zero(current_string, number_length, array_to_record)
            recursion_add_one(current_string, number_length, array_to_record)


def find_all(number):
    record = []
    recursion("", number, record)
    print(record)


def solve():
    n = int(input())
    find_all(n)


if __name__ == "__main__":
    solve()
