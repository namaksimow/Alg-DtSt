import string
import random


def get_second_priority(first_priority, second_priority, third_priority, global_alphabet, tasks):
    alphabet = global_alphabet[first_priority + second_priority: first_priority + second_priority + third_priority]
    for i in range(second_priority):
        tasks[global_alphabet[first_priority + i]] = get_random_letter(second_priority, third_priority, alphabet)


def get_first_priority(first_priority, second_priority, third_priority, global_alphabet, tasks):
    alphabet = global_alphabet[first_priority: first_priority + second_priority + third_priority]
    for i in range(first_priority):
        tasks[global_alphabet[i]] = get_random_letter(first_priority, second_priority, alphabet)


def get_random_letter(start_range, end_range, alphabet):
    random_letters = set()
    for i in range(start_range):
        count_dependency = random.randint(1, end_range)
        while len(random_letters) < count_dependency:
            random_letter = random.choice(alphabet)
            random_letters.add(random_letter)
    result = ''.join(sorted(random_letters))

    return result


def fill_tasks(tasks, first_priority, second_priority, third_priority, global_alphabet):
    get_first_priority(first_priority, second_priority, third_priority, global_alphabet, tasks)
    get_second_priority(first_priority, second_priority, third_priority, global_alphabet, tasks)


def fill_tasks_priority(tasks, tasks_priority, first_priority, second_priority, third_priority, global_alphabet):
    fp = global_alphabet[:first_priority]
    fp_dict = {}
    fp_list = []
    fp_letter = []
    for i in range(len(fp)):
        fp_dict[fp[i]] = tasks[fp[i]]
    for key in fp_dict:
        fp_list.append(fp_dict[key])
        fp_letter.append(key)
    for i in range(len(fp_list) - 1):
        for j in range(len(fp_list) - i - 1):
            if fp_list[j] < fp_list[j + 1]:
                fp_list[j], fp_list[j + 1] = fp_list[j + 1], fp_list[j]
                fp_letter[j], fp_letter[j + 1] = fp_letter[j + 1], fp_letter[j]

    sp = global_alphabet[first_priority: first_priority + second_priority]
    sp_dict = {}
    sp_list = []
    sp_letter = []
    for i in range(len(sp)):
        sp_dict[sp[i]] = tasks[sp[i]]
    for key in sp_dict:
        sp_list.append(sp_dict[key])
        sp_letter.append(key)
    for i in range(len(sp_list) - 1):
        for j in range(len(sp_list) - i - 1):
            if sp_list[j] < sp_list[j + 1]:
                sp_list[j], sp_list[j + 1] = sp_list[j + 1], sp_list[j]
                sp_letter[j], sp_letter[j + 1] = sp_letter[j + 1], sp_letter[j]

    tp = global_alphabet[first_priority + second_priority: first_priority + second_priority + third_priority]

    for i in range(1, third_priority + 1):
        tasks_priority[i] = tp[i - 1]
    for i in range(third_priority + 1, third_priority + second_priority + 1):
        tasks_priority[i] = sp_letter[i - third_priority - 1]
    for i in range(third_priority + second_priority + 1, third_priority + second_priority + first_priority + 1):
        tasks_priority[i] = fp_letter[i - third_priority - second_priority - 1]


def create_dependency(first_priority, second_priority, third_priority):
    tasks = {letter: "" for letter
             in list(string.ascii_uppercase)[:first_priority + second_priority + third_priority]}
    tasks_priority = {number: "" for number in range(1, first_priority + second_priority + third_priority + 1)}
    global_alphabet = list(string.ascii_uppercase)

    fill_tasks(tasks, first_priority, second_priority, third_priority, global_alphabet)

    for key in tasks:
        print(key, tasks[key], len(tasks[key]))

    fill_tasks_priority(tasks, tasks_priority, first_priority, second_priority, third_priority, global_alphabet)
    print(tasks_priority)


def solve():
    first_priority = int(input("Input tasks first priority "))
    second_priority = int(input("Input tasks second priority "))
    third_priority = int(input("Input tasks third priority "))
    create_dependency(first_priority, second_priority, third_priority)


if __name__ == "__main__":
    solve()
