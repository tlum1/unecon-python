import json

TASKS_FILE = 'tasks.json'

def read_tasks():
    with open(TASKS_FILE, 'r') as f:
        tasks = json.load(f)
    return tasks

def write_tasks(tasks):
    try:
        with open(TASKS_FILE, 'w') as f:
            tasks = json.dump(tasks, f)
        print('Задачи сохранены в файл!')
    except Exception as e:
        print(e)

def add_task(tasks):
    name = input('Сформулируйте задачу: ')
    category = input('Добавьте категорию к задаче: ')
    time = input('Добавьте время к задаче: ')
    tasks.append({'name': name, 'category': category, 'time': time})

if __name__ == "__main__":  
    tasks = read_tasks()

    print('Текущие задачи из файла:')
    print(tasks)

    while True:
        print('''Простой todo: 
        1. Добавить задачу.
        2. Вывести список задач.
        3. Выход.''')
        arg = int(input('Укажите число: '))
        if arg == 1:
            add_task(tasks)
        elif arg == 2:
            if len(tasks) == 0:
                print('В списке нет задач.')
            for task in tasks:
                print(f'Задача: {task["name"]} Категория: {task["category"]} Дата: {task["time"]}')
        elif arg == 3:
            write_tasks(tasks)
            break
