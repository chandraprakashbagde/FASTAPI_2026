from fastapi import FastAPI, Form
from fastapi.responses import HTMLResponse
from typing import Annotated

app = FastAPI()

@app.get("/", response_class=HTMLResponse)
async def login_form():
    return """
    <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Login Form</title>
        </head>
        <body>

            <h2>Login Form</h2>
            <form action="/login/" method="post">
                <label for="username">Username:</label><br>
                <input type="text" id="username" name="username"><br>
                <label for="password">Password:</label><br>
                <input type="password" id="password" name="password"><br><br>
                <input type="submit" value="Submit">
            </form>

        </body>
    </html>
    """

@app.post("/login")
async def user_login(username: Annotated[str, Form()], password: Annotated[str, Form()]):
    return {
        "username":username,
        "password":password
    }
