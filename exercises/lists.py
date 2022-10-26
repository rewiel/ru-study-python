from math import inf


class ListExercise:
    @staticmethod
    def replace(input_list: list[int]) -> list[int]:
        """
        Заменить все положительные элементы целочисленного списка на максимальное значение
        элементов списка.
        :param input_list: Исходный список
        :return: Список с замененными элементами
        """

        return [_ if _ <= 0 else ListExercise._list_max_enum(input_list) for _ in input_list]

    @classmethod
    def _list_max_enum(cls, input_list: list[int]) -> float:
        item_max = -inf
        for item in input_list:
            item_max = item_max if item_max > item else item

        return item_max

    @staticmethod
    def search(input_list: list[int], query: int) -> int:
        """
        Реализовать двоичный поиск
        Функция должна возвращать индекс элемента
        :param input_list: Исходный список
        :param query: Искомый элемент
        :return: Номер элемента
        """

        return ListExercise._binary_search(input_list, 0, len(input_list) - 1, query)

    @classmethod
    def _binary_search(cls, recursive_list: list[int], low: int, high: int, query: int) -> int:

        if high >= low:

            mid_index = (low + high) // 2
            mid_value = recursive_list[mid_index]

            if query > mid_value:
                return ListExercise._binary_search(recursive_list, mid_index + 1, high, query)
            elif query < mid_value:
                return ListExercise._binary_search(recursive_list, low, mid_index - 1, query)
            else:
                return mid_index

        else:
            return -1
