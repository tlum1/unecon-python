def print_shelfs() -> None:
    print("Текущий перечень полок:", end=" ")
    for key in directories:
        print(f"{key}, ", end=" ")


def add_to_shelf(shelf_number: str, doc_number: str) -> bool:
    if shelf_number not in directories.keys():
        print("такой полки не существует. Добавьте полку командой as.")
        return False
    else:
        directories[shelf_number].append(doc_number)
        return True


def get_shelf(doc_number: str) -> str:
    for key, value in directories.items():
        if doc_number in value:
            return key
    else:
        print("Документ не найден в базе")


def document_index(doc_number: str) -> int:
    item_index = -1
    for i in range(len(documents)):
        if documents[i]["number"] == doc_number:
            item_index = i
    if item_index == -1:
        print("Документ не найден")
    return item_index


def task_1_1(doc_number: str) -> None:
    for item in documents:
        if item["number"] == doc_number:
            print("Владелец документа:", item["name"])
            break
    else:
        print("Документ не найден в базе")


def task_1_2(doc_number: str) -> str:
    for key, value in directories.items():
        if doc_number in value:
            print("Документ хранится на полке", key)
            return key
    else:
        print("Документ не найден в базе")


def task_1_3() -> None:
    for item in documents:
        print(
            f"№ {item['number']}, тип: {item['type']}, владелец: {item['name']}, полка хранения: {get_shelf(item['number'])}")


def task_1_4(shelf_number: str) -> None:
    directories[shelf_number] = []
    print("Полка добавлена")
    print_shelfs()


def task_1_5(shelf_number: str) -> None:
    if shelf_number not in directories.keys():
        print("такой полки не существует")
    elif not directories[shelf_number]:
        directories.pop(shelf_number)
        print("Полка удалена")
    else:
        print("На полке есть документы, удалите их перед тем как удалять полку")
    print_shelfs()


def task_2_1(item: dict, shelf_number: str) -> None:
    documents.append(item)
    if add_to_shelf(shelf_number, item["number"]):
        print("Документ добавлен")
        task_1_3()


def task_2_2(doc_number: str) -> None:
    item_index = document_index(doc_number)

    if item_index > -1:
        print("Документ удален")
        documents.pop(item_index)
        shelf_number = get_shelf(doc_number)
        directories[shelf_number].pop(directories[shelf_number].index(doc_number))
    task_1_3()


def task_2_3(doc_number: str, shelf_number: str):
    item_index = document_index(doc_number)
    if shelf_number in directories.keys() and item_index > -1:
        old_shelf_number = get_shelf(doc_number)
        directories[old_shelf_number].pop(directories[old_shelf_number].index(doc_number))
        directories[shelf_number].append(doc_number)
    elif shelf_number not in directories.keys():
        print("полка не найдена")
        print_shelfs()
    elif item_index == -1:
        print("Документ не найден в базе")
    task_1_3()


documents = [
    {'type': 'passport', 'number': '2207 876234', 'name': 'Василий Гупкин'},
    {'type': 'invoice', 'number': '11-2', 'name': 'Геннадий Покемонов'},
    {'type': 'insurance', 'number': '10006', 'name': 'Аристарх Павлов'}
]

directories = {
    '1': ['2207 876234', '11-2'],
    '2': ['10006'],
    '3': []
}

while True:
    command = input("Введите команду ")
    if command == "p":
        doc_number = input("Введите номер документа ")
        task_1_1(doc_number)
    elif command == "s":
        doc_number = input("Введите номер документа ")
        task_1_2(doc_number)
    elif command == "l":
        task_1_3()
    elif command == "ads":
        shelf_number = input("Введите номер полки ")
        task_1_4(shelf_number)
    elif command == "ds":
        shelf_number = input("Введите номер полки ")
        task_1_5(shelf_number)
    elif command == "ad":
        doc_number = input("Введите номер документа ")
        doc_type = input("Введите тип документа ")
        doc_owner = input("Введите владельца документа ")
        shelf_number = input("Введите номер полки ")
        task_2_1({'type': doc_type, 'number': doc_number, 'name': doc_owner}, shelf_number)
    elif command == "d":
        doc_number = input("Введите номер документа ")
        task_2_2(doc_number)
    elif command == "m":
        doc_number = input("Введите номер документа ")
        shelf_number = input("Введите номер полки ")
        task_2_3(doc_number, shelf_number)
    elif command == "q":
        break
