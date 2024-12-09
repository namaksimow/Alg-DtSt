import string
alphabet = list(string.ascii_uppercase)


def input_dependency():
    n = int(input("Input count projects"))
    tasks = {}
    priority = {}
    for i in range(n):
        depend = list(map(str, input().split()))
        letter = depend[0]
        dependency = depend[1]
        if letter not in tasks:
            tasks[letter] = dependency
            priority[letter] = 0

    return tasks, priority


def get_first_priority(tasks, priority):
    priority_work = {}
    priority_work_index = 1
    priority_index = 1
    key_to_delete = []
    for key in tasks:
        if tasks[key] == "empty":
            priority[key] = priority_index
            priority_index += 1
            key_to_delete.append(key)

    for key in key_to_delete:
        if key in tasks:
            del tasks[key]
    key_to_delete = key_to_delete[::-1]
    priority_work[priority_work_index] = key_to_delete
    return tasks, priority, priority_index, priority_work, priority_work_index


def get_second_priority(tasks, priority, priority_index, priority_work, priority_work_index):
    key_to_delete = []
    key_value_to_delete = []
    for key in tasks:
        letters = tasks[key]
        is_convert = check_string(letters, priority)
        if is_convert:
            new_letters = replace_string(letters, priority)
            tasks[key] = new_letters
            key_to_delete.append(key)
            key_value_to_delete.append(new_letters)

    key_value_to_delete, key_to_delete = sort_values(key_value_to_delete, key_to_delete)
    for key in key_to_delete:
        if key in tasks:
            del tasks[key]
            priority[key] = priority_index
            priority_index += 1

    key_to_delete = key_to_delete[::-1]
    priority_work_index += 1
    priority_work[priority_work_index] = key_to_delete
    return tasks, priority, priority_index, priority_work, priority_work_index


def sort_values(values_list, key_list):
    n = len(values_list)
    for i in range(n):
        for j in range(n - i - 1):
            if values_list[j] > values_list[j + 1]:
                values_list[j], values_list[j + 1] = values_list[j + 1], values_list[j]
                key_list[j], key_list[j + 1] = key_list[j + 1], key_list[j]
    return values_list, key_list


def check_string(string_to_check, priority):
    for i in range(len(string_to_check)):
        char = string_to_check[i]
        if priority[char] == 0:
            return False

    return True


def replace_string(old_string, priority):
    new_letters = ""
    for i in range(len(old_string)):
        char = old_string[i]
        if char in priority and priority[char] != 0:
            new_letters += str(priority[char])

    sorted_digits = sorted(new_letters, reverse=True)
    result = ''.join(sorted_digits)
    return result


def appoint_employee(priority, work):
    work = dict(sorted(work.items(), key=lambda item: item[0], reverse=True))
    priority = sorted(priority, key=priority.get, reverse=True)
    employee1 = [0 for _ in range(len(priority))]
    employee2 = [0 for _ in range(len(priority))]
    e1index = 0
    e2index = 0
    for key in work:
        works = work[key]
        for i in range(len(works)):
            if e1index > e2index:
                employee2[e2index] = works[i]
                e2index += 1
            else:
                employee1[e1index] = works[i]
                e1index += 1

        if len(works) == 1:
            e1index = max(e1index, e2index)
            e2index = e1index

    return employee1, employee2


def solve():
    tasks, priority = input_dependency()
    tasks, priority, priority_index, work, work_index = get_first_priority(tasks, priority)

    while len(tasks) > 0:
        tasks, priority, priority_index, work, work_index \
            = get_second_priority(tasks, priority, priority_index, work, work_index)

    e1, e2 = appoint_employee(priority, work)
    print(f"\nfirst employee - {e1}")
    print(f"second employee - {e2}")


if __name__ == "__main__":
    solve()
