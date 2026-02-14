"""
Третье упражнение главы 4
Нужно написать рекурсивную функцию, которая возвращает наибольший элемент массива
"""


def max_number_in_list(
    any_list: list[int], max_number: int | None = None, index: int = 0
) -> int | None:
    """
    Здесь мы рекурсивно должны найти наибольший элемент массива и вернуть его
    :param any_list:
    :param max_number:
    :param index:
    :return: int
    """
    if not any_list:
        return None

    if max_number is None:
        max_number = any_list[index]

    if len(any_list) - 1 < index:
        return max_number

    if max_number < any_list[index]:
        max_number = any_list[index]
    return max_number_in_list(any_list, max_number, index + 1)


print(max_number_in_list([1, 2, 8, 6, 6, 7]))
