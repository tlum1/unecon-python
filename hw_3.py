import random


def task_1() -> None:
    hidden_number = random.randint(1, 10)
    print(hidden_number)
    while True:
        answer = int(input("Введите загаданное число "))
        if answer == hidden_number:
            print("Вы победили!")
            break
        else:
            print("Загаданное число больше" if answer < hidden_number else "Загаданное число меньше")


# task_1()

def task_2() -> str:
    random_length = random.randint(7, 10)
    password = ""
    for i in range(random_length):
        password += chr(random.randint(33, 126))
    return password


# print(task_2())

def task_3(password: str) -> bool:
    return len(password) > 7 and any([i.isupper() for i in password]) and any([i.lower() for i in password])


# print(task_3("123sbffh"))

def task_4() -> None:
    attempts = 0
    while True:
        attempts += 1
        password = task_2()
        if task_3(password):
            print(attempts)
            break

# task_4()
