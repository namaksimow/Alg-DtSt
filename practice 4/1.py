import random
import string


# sorting tasks by time, if ai > bi : first else: second
def grouping_by_time(tasks: dict) -> (dict, dict):
    first_group = {}
    second_group = {}
    for key in tasks:
        time_tuple = tasks[key]
        if time_tuple[0] <= time_tuple[1]:
            first_group[key] = tasks[key]
        else:
            second_group[key] = tasks[key]
    return first_group, second_group


# input duration for 1 and 2 second employee
def input_task_time(count_task: int) -> dict:
    alphabet = list(string.ascii_lowercase)
    tasks: dict = {}
    for i in range(count_task):
        tasks[alphabet[i].upper()] = (i + 1, random.randint(1, count_task))

    return tasks


# sorting first group by ascending, second group by descending
def sort_group(first_group, second_group):
    first_group = dict(sorted(first_group.items(), key=lambda pair: pair[1][0]))
    second_group = dict(sorted(second_group.items(), key=lambda pair: pair[1][0], reverse=True))
    general_group = {**first_group, ** second_group}
    return general_group


def start_time(general_group):
    time_end_first = 0
    key = next(iter(general_group))
    value = general_group[key][0]
    time_end_second = value
    return time_end_first, time_end_second


# point tasks between two employees
def task_distribution(general_group):
    time_end_first, time_end_second = start_time(general_group)
    
    first_employee = {}
    second_employee = {}
    for key in general_group:
        pair_tuple = general_group[key]
        first_employee[key] = (time_end_first, time_end_first + pair_tuple[0])
        if time_end_first + pair_tuple[0] <= time_end_second:
            second_employee[key] = (time_end_second, time_end_second + pair_tuple[1])
        else:
            second_employee[key] = (time_end_first + pair_tuple[0], time_end_first + pair_tuple[0] + pair_tuple[1])
        time_end_first += pair_tuple[0]
        time_end_second += pair_tuple[1]

    return general_group, first_employee, second_employee


def print_answer(general_group, first_employee, second_employee):
    print(f"{general_group} - all tasks\n\n{first_employee} - first employee\n\n{second_employee} - second employee")


def solve():
    n = int(input("Input count tasks "))
    task_dict = input_task_time(n)
    first_group, second_group = grouping_by_time(task_dict)
    general_group = sort_group(first_group, second_group)
    general_group, first_employee, second_employee = task_distribution(general_group)
    print_answer(general_group, first_employee, second_employee)


if __name__ == "__main__":
    solve()
