"""
Здесь я сам реализую сортировку выбором
"""


def min_item(any_array: list) -> int:
    """
    Вынес нахождение минимального элемента списка в отдельную функцию.
    Возвращает индекс минимального элемента
    :param any_array:
    :return: index_item
    """
    small_item = any_array[0]
    index_item = 0

    for index, item in enumerate(any_array, start=0):
        if item < small_item:
            small_item = item
            index_item = index

    return index_item


def select_sort(any_array: list) -> list:
    """
    Функция сортировки выбором
    вернет новый отсортированный список по возрастанию
    """

    sorted_array = []
    for _ in range(len(any_array)):
        sorted_array.append(any_array.pop(min_item(any_array)))

    return sorted_array


print(select_sort([1, 4, 6, 2, 7, 6]))
