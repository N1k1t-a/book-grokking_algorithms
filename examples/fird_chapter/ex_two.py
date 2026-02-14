"""
Второе упражнение главы 4
Нужно написать рекурсивную функцию для подсчета количества элементов в списке
"""


def count_item_list(my_list: list[int], index: int = 0) -> int:
    """
    Функция подсчета количества элементов в списке
    :param my_list:
    :param index:
    :return: int
    """

    if not my_list:
        return 0

    if len(my_list) - 1 == index:
        return 1

    return 1 + count_item_list(my_list, index + 1)


print(count_item_list([1, 2, 4, 6, 6, 7]))


def quick_count_item_list(
    my_list: list[int], left: int = 0, right: int | None = None
) -> int:
    """
    Функция подсчета количества элементов в списке. Метод разделяй и властвуй
    :param right:
    :param left:
    :param my_list:
    :return: int
    """
    if right is None:
        right = len(my_list) - 1

    if left > right:
        return 0

    if right == left:
        return 1

    mid = (right + left) // 2
    return quick_count_item_list(my_list, left, mid) + quick_count_item_list(
        my_list, mid + 1, right
    )


print(quick_count_item_list([1, 2, 4, 6, 6, 7]))
