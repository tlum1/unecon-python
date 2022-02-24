import random


def task_5():
    words = ['самовар', 'весна', 'лето']
    guess_word = random.choice(words)
    random_letter_index = random.randint(0, len(guess_word) - 1)
    guess_word = guess_word[0:random_letter_index] + "?" + guess_word[random_letter_index + 1:]
    print(guess_word)
    letter = input("Введите букву ")
    if guess_word.replace("?", letter) in words:
        print("Победа!")
    else:
        print("Вы проиграли")


# task_5()
def task_6(text):
    print("Количество строк - ", len(text.split("\n")))
    print(f"Количество слов - ", len(text))


text = """В тот год осенняя погода
    Стояла долго на дворе
    Зимы ждала ждала природа
    Снег выпал только в январе
    На третье в ночь Проснувшись рано
    В окно увидела Татьяна
    Поутру побелевший двор
    Куртины, кровли и забор
    На стеклах легкие узоры
    Деревья в зимнем серебре
    Сорок веселых на дворе
    И мягко устланные горы
    Зимы блистательным ковром
    Все ярко, все бело кругом"""

task_6(text)
