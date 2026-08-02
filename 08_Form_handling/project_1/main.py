from fastapi import FastAPI, Form, File, UploadFile, Path
from fastapi.responses import HTMLResponse
from typing import Annotated, List
from pydantic import BaseModel

import os
import uuid
import shutil

users = []

app = FastAPI()


def empty_directory(directory_path: str):
    if not os.path.exists(directory_path):
        return

    for item in os.listdir(directory_path):
        item_path = os.path.join(directory_path, item)

        try:
            if os.path.isfile(item_path) or os.path.islink(item_path):
                os.remove(item_path)  # Delete file or symlink
            elif os.path.isdir(item_path):
                shutil.rmtree(item_path)  # Delete subdirectory
        except Exception as e:
            print(f"Failed to delete {item_path}: {e}")

@app.get("/",response_class=HTMLResponse)
async def main():
    rows = ""

    for user in users:
        rows+= f"""
            <tr>
                <td>{user["username"]}</td>
                <td>{user["userid"]}</td>
                <td><a href="/update_aadhar/{user["userid"]}">>>></a></td>
                <td><a href="/update_pan/{user["userid"]}">>>></a></td>
            </tr>
            """

    return f"""
        <!DOCTYPE html>
        <html>
        <head>
            <title>Basic Table</title>
        </head>
        <body>

            <table border="1" style="width:50%;margin:auto;">
                <tr>
                    <th>Username</th>
                    <th>User ID</th>
                    <th>Update Aadhar</th>
                    <th>Update Pan</th>
                </tr>
                {rows}
            </table>

        </body>
        </html>
        """

@app.get("/add-edit-user", response_class=HTMLResponse)
async def main():
    return """
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>User Form</title>
        </head>
        <body>

            <h2>User Details</h2>

            <form action="/api/create-user" method="post" enctype="multipart/form-data">
                <div>
                    <label for="username">Username:</label><br>
                    <input
                        type="text"
                        id="username"
                        name="username"
                        required
                    >
                </div>

                <br>

                <div>
                    <label for="aadhaar">Aadhaar Files:</label><br>
                    <input
                        type="file"
                        id="aadhaar"
                        name="aadhaar_files"
                        multiple
                    >
                </div>

                <br>

                <div>
                    <label for="pan">PAN Files:</label><br>
                    <input
                        type="file"
                        id="pan"
                        name="pan_files"
                        multiple
                    >
                </div>

                <br>

                <button type="submit">Submit</button>
            </form>

        </body>
        </html>
    """

@app.get("/update_aadhar/{userid}", response_class=HTMLResponse)
async def main(userid: Annotated[str, Path()]):
    return f"""
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Update Aadhar Card</title>
        </head>
        <body>

            <h2>User Details</h2>

            <form action="/api/aadhar_update/{userid}" method="post" enctype="multipart/form-data">
                <div>
                    <label for="aadhaar">Aadhaar Files:</label><br>
                    <input
                        type="file"
                        id="aadhaar"
                        name="aadhar_files"
                        multiple
                    >
                </div>

                <br>

                <button type="submit">Submit</button>
            </form>

        </body>
        </html>
    """

@app.get("/update_pan/{userid}", response_class=HTMLResponse)
async def main(userid: Annotated[str, Path()]):
    return f"""
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Update Aadhar Card</title>
        </head>
        <body>

            <h2>User Details</h2>

            <form action="/api/pan_update/{userid}" method="post" enctype="multipart/form-data">
                <div>
                    <label for="pan">Pan Files:</label><br>
                    <input
                        type="file"
                        id="pan"
                        name="pan_files"
                        multiple
                    >
                </div>

                <br>

                <button type="submit">Submit</button>
            </form>

        </body>
        </html>
    """



## APIs.
@app.post("/api/create-user")
async def create_user(
    username: Annotated[str, Form(min_length=5)],
    aadhaar_files: Annotated[list[UploadFile], File(min_length=2,max_length=2)],
    pan_files: Annotated[list[UploadFile], File(min_length=2, max_length=2)]
):
    userid = uuid.uuid4()
    dir = f"08_Form_handling/project_1/upload/{userid}"
    os.makedirs(dir, exist_ok=True)
    for file in aadhaar_files:
        aadhaar_dir = f"{dir}/aadhar_files"
        os.makedirs(aadhaar_dir, exist_ok=True)
        save_path = f"{aadhaar_dir}/{file.filename}"
        with open(save_path, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)

    for file in pan_files:
        pan_dir = f"{dir}/pan_files"
        os.makedirs(pan_dir, exist_ok=True)
        save_path = f"{pan_dir}/{file.filename}"
        with open(save_path, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)

    users.append({
        "username":username,
        "userid":userid
    })

    return {
        "username":username,
        "aadhaar_files":aadhaar_files,
        "pan_files":pan_files
    }

@app.post("/api/aadhar_update/{userid}")
async def aadhar_update(userid:Annotated[str, Path()], aadhar_files:Annotated[list[UploadFile], File(min_length=2)]):
    dir = f"08_Form_handling/project_1/upload/{userid}/aadhar_files"
    for filename in next(os.walk(dir))[2]:
        os.remove(f"{dir}/{filename}")

    for file in aadhar_files:
        with open(f"{dir}/{file.filename}", "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)

@app.post("/api/pan_update/{userid}")
async def pan_update(userid:Annotated[str, Path()], pan_files:Annotated[list[UploadFile], File(min_length=2)]):
    dir = f"08_Form_handling/project_1/upload/{userid}/pan_files"
    for filename in next(os.walk(dir))[2]:
        os.remove(f"{dir}/{filename}")

    for file in pan_files:
        with open(f"{dir}/{file.filename}", "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)