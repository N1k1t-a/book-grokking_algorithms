"""
Здесь я запишу функцию бинарного поиска. Это основная тема первой главы.
функция будет принимать отсортированный список и число которое требуется найти
ВАЖНО: что бинарный поиск работает только с отсортированными массивами
"""

from typing import Callable
from functools import wraps
from time import time


def check_time(func: Callable) -> Callable:
    """Декоратор для измерения времени выполнения функции"""

    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time()
        result = func(*args, **kwargs)
        out_time = time()
        print(f"Время выполнения кода {out_time - start_time:.6f}")
        return result

    return wrapper


@check_time
def binary_search(sorted_array, item) -> int | None:
    """
    Эта функция принимает на вход отсортированный массив и элемент, который требуется найти
    функция ищет нужный элемент при помощи бинарного поиска.
    Возвращает индекс элемента списка, если такой имеется, иначе None

    :param sorted_array:
    :param item:
    :return: index_item | None
    """

    low = 0
    high = len(sorted_array) - 1

    while low <= high:
        mid = (low + high) // 2

        if sorted_array[mid] == item:
            return mid
        if sorted_array[mid] > item:
            high = mid - 1
        else:
            low = mid + 1

    return None


if __name__ == "__main__":
    my_array = list(range(1, 100000001))

    item_place = binary_search(my_array, 1245220)
    print(my_array[item_place], "aboba", item_place)
