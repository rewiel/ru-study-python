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

        def _list_max_enum(input_list: list[int]) -> int:
            item_max = -inf
            if len(input_list) > 0:
                for item in input_list:
                    item_max = item_max if item_max > item else item
                return int(item_max)
            return None

        max_el = _list_max_enum(input_list)
        return [item if item <= 0 else max_el for item in input_list]

    @staticmethod
    def search(input_list: list[int], query: int) -> int:
        """
        Реализовать двоичный поиск
        Функция должна возвращать индекс элемента
        :param input_list: Исходный список
        :param query: Искомый элемент
        :return: Номер элемента
        """

        def _binary_search(recursive_list: list[int], low: int, high: int, query: int) -> int:

            if high >= low:

                mid_index = (low + high) // 2
                mid_value = recursive_list[mid_index]

                if query > mid_value:
                    return _binary_search(recursive_list, mid_index + 1, high, query)
                elif query < mid_value:
                    return _binary_search(recursive_list, low, mid_index - 1, query)
                else:
                    return mid_index

            else:
                return -1

        return _binary_search(input_list, 0, len(input_list) - 1, query)
