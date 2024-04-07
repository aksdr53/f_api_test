from fastapi import FastAPI

from models.models import User

app = FastAPI()

user = User(
    id=1,
    name='John Doe',
)

# пример роута (маршрута)
@app.get("/")
def read_root():
    return {"message": "Hello, World!"}


@app.get("/custom")
def read_custom_message():
    return {"message": "This is a custom message!"}


@app.get("/users")
def get_user():
    return user