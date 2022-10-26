from typing import Union


class MapExercise:
    @staticmethod
    def rating(list_of_movies: list[dict]) -> float:
        """
        !!Задание нужно решить используя map!!
        Посчитать средний рейтинг фильмов (rating_kinopoisk), у которых две или больше стран.
        Фильмы у которых рейтинг не задан или равен 0 не учитывать в расчете среднего.
        :param list_of_movies: Список фильмов.
        Ключи словаря: name, rating_kinopoisk, rating_imdb, genres, year, access_level, country
        :return: Средний рейтинг фильмов у которых две или больше стран
        """

        def _filter_rating(movie: dict[str, str]) -> float:
            """ """

            try:
                if (
                    movie.get("rating_kinopoisk").replace(" ", "") != ""
                    and float(movie.get("rating_kinopoisk")) != 0
                    and len(
                        list(filter(lambda x: x, movie.get("country").replace(" ", "").split(",")))
                    )
                    >= 2
                ):
                    return float(movie.get("rating_kinopoisk"))
                else:
                    return None
            except ValueError as e:
                print(
                    f"""{e} - в строчке с назвнаием фильма {movie.get("name")},
                     значение в столбце rating_kinopoisk = {movie.get("rating_kinopoisk")}"""
                )
                return None

        list_of_rating = list(filter(lambda x: x, list(map(_filter_rating, list_of_movies))))
        return sum(list_of_rating) / len(list_of_rating)

    @staticmethod
    def chars_count(
        list_of_movies: list[dict], rating: Union[float, int], symbol: str = "и"
    ) -> int:
        """
        !!Задание нужно решить используя map!!
        Посчитать количество букв 'и' в названиях всех фильмов с рейтингом (rating_kinopoisk) больше
        или равным заданному значению
        :param list_of_movies: Список фильмов
        Ключи словаря: name, rating_kinopoisk, rating_imdb, genres, year, access_level, country
        :param rating: Заданный рейтинг
        :return: Количество букв 'и' в названиях всех фильмов с рейтингом больше
        или равным заданному значению
        """

        def _filter_rating(movie: dict[str, str]) -> int:
            """ """

            try:
                if (
                    movie.get("rating_kinopoisk").replace(" ", "") != ""
                    and float(movie.get("rating_kinopoisk", 0)) > rating
                ):
                    return movie.get("name").count(symbol)
                else:
                    return 0
            except ValueError as e:
                print(
                    f"""{e} - в строчке с назвнаием фильма {movie.get("name")},
                     значение в столбце rating_kinopoisk = {movie.get("rating_kinopoisk")}"""
                )
                return None

        return sum(list(map(_filter_rating, list_of_movies)))
