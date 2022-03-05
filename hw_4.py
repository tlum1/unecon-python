import math, statistics


def my_log(numbers: list) -> list:
    return [math.log(x) if x > 0 else None for x in numbers]


print(my_log([1, 3, 2.5, -1, 9, 0, 2.71]))


def task_17(numbers: list) -> list:
    max_ind = numbers.index(max(numbers))
    min_ind = numbers.index(min(numbers))
    if max_ind < min_ind:
        return [statistics.median(numbers)] * len(numbers)
    else:
        return statistics.mean(numbers[min_ind + 1:max_ind])


print(task_17([1, 2, 3]))


def task_19(numbers: list) -> list:
    mean = statistics.mean([x for x in numbers if x])
    return [x if x else mean for x in numbers]


print(task_19([1, 5, 6.3, 6, None, 2.0, -4, None]))


def task_11(text: str) -> list:
    return [[word for word in sentence.split() if len(word) > 3] for sentence in text.split("\n")]


print(task_11('''Call me Ishmael. Some years ago - never mind how long precisely - having
little or no money in my purse, and nothing particular to interest me
on shore, I thought I would sail about a little and see the watery part
of the world. It is a way I have of driving off the spleen, and regulating
the circulation. - Moby Dick'''
              ))
