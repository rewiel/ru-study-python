from flask import Flask
from flask import request
from flask import Response
from flask import make_response
import json


class FlaskExercise:
    """
    Вы должны создать API для обработки CRUD запросов.
    В данной задаче все пользователи хранятся в одном словаре, где ключ - это имя пользователя,
    а значение - его параметры. {"user1": {"age": 33}, "user2": {"age": 20}}
    Словарь (dict) хранить в памяти, он должен быть пустым при старте flask.

    POST /user - создание пользователя.
    В теле запроса приходит JSON в формате {"name": <имя пользователя>}.
    Ответ должен вернуться так же в JSON в формате {"data": "User <имя пользователя> is created!"}
    со статусом 201.
    Если в теле запроса не было ключа "name", то в ответ возвращается JSON
    {"errors": {"name": "This field is required"}} со статусом 422

    GET /user/<name> - чтение пользователя
    В ответе должен вернуться JSON {"data": "My name is <name>"}. Статус 200

    PATCH /user/<name> - обновление пользователя
    В теле запроса приходит JSON в формате {"name": <new_name>}.
    В ответе должен вернуться JSON {"data": "My name is <new_name>"}. Статус 200

    DELETE /user/<name> - удаление пользователя
    В ответ должен вернуться статус 204
    """

    USERS: dict[str, dict] = {}

    app = Flask(__name__)

    @staticmethod
    def configure_routes(app: Flask) -> None:
        app.post("/user")(FlaskExercise.create_user)
        app.get("/user/<name>")(FlaskExercise.get_user)
        app.patch("/user/<name>")(FlaskExercise.update_user)
        app.delete("/user/<name>")(FlaskExercise.delete_user)

    @staticmethod
    def create_user() -> Response:
        content = request.get_json()
        if name := content.pop("name", None):
            FlaskExercise.USERS[name] = content
            return make_response({"data": f"User {name} is created!"}, 201)
        else:
            return Response(
                response=json.dumps({"errors": {"name": "This field is required"}}),
                status=422,
                content_type="application/json",
            )

    @staticmethod
    def get_user(name: str) -> Response:
        if name in FlaskExercise.USERS.keys():
            return make_response({"data": f"My name is {name}"}, 200)
        else:
            return make_response({"errors": {"name": f"This name {name} wasn't found"}}, 404)

    @staticmethod
    def update_user(name: str) -> Response:
        if name in FlaskExercise.USERS.keys():
            new_name = request.get_json()["name"]
            FlaskExercise.USERS[new_name] = FlaskExercise.USERS.pop(name)
            return make_response({"data": f"My name is {new_name}"}, 200)
        else:
            return make_response({"errors": {"name": f"This name {name} wasn't found"}}, 404)

    @staticmethod
    def delete_user(name: str) -> Response:
        if name in FlaskExercise.USERS.keys():
            FlaskExercise.USERS.pop(name)
            return make_response("", 204)
        else:
            return make_response({"errors": {"name": f"This name {name} wasn't found"}}, 404)
