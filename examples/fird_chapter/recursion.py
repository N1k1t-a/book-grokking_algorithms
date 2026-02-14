"""
Первое упражнение главы 4
Нужно написать рекурсивную функцию для суммы всех элементов массива
"""


def recursion_sum(my_array: list[int], index: int = 0) -> int:
    """
    Рекурсивная функция, принимает список, возвращает сумму элементов списка
    :param index:
    :param my_array:
    :return: int
    """

    if index >= len(my_array):
        return 0

    return my_array[index] + recursion_sum(my_array, index + 1)


print(recursion_sum([1, 2, 4, 6, 6, 7]))


def quick_sum(my_array: list[int], left: int = 0, right: int | None = None) -> int:
    """
    Это быстрый подсчет. Применяю метод "Разделяй и властвуй"
    :param my_array:
    :param left:
    :param right:
    :return: int
    """

    if right is None:
        right = len(my_array) - 1

    if left > right:
        return 0

    if right == left:
        return my_array[left]

    mid = (left + right) // 2
    return quick_sum(my_array, left, mid) + quick_sum(my_array, mid + 1, right)


print(quick_sum([1, 2, 4, 6, 6, 7]), "на движениях")
