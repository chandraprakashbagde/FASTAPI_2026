from fastapi import FastAPI, Form, File, UploadFile
from fastapi.responses import HTMLResponse
from typing import Annotated, List
from pydantic import BaseModel, Field

import os
import uuid
import shutil

app = FastAPI()

## Signle File Upload with "bytes" type
# @app.get("/", response_class=HTMLResponse)
# async def main():
#     return """
#     <html>
#         <body>
#             <h2>Single File Upload (bytes)</h2>
#             <form action="/files" enctype="multipart/form-data" method="post">
#                 <input name="file" type="file">
#                 <input type="submit" value="Upload">
#             </form>
#         </body>
#     </html>
# """

# @app.post("/files")
# async def create_file(file: Annotated[bytes | None, File()]):
#     if not file:
#         return { 
#             "message" : "No file sent"
#         }

#     filename = f"{uuid.uuid4()}.bin"
#     save_path = f"uploads/{filename}"

#     os.makedirs("uploads", exist_ok=True)

#     with open(save_path, "wb") as buffer:
#         buffer.write(file)
    
#     return {
#         "file size":len(file)
#     }

## File Upload with with "UploadFile" type
# @app.get("/", response_class=HTMLResponse)
# async def main():
#     return """
#     <html>
#         <body>
#             <h2>Single File Upload (bytes)</h2>
#             <form action="/uploads" enctype="multipart/form-data" method="post">
#                 <input name="file" type="file">
#                 <input type="submit" value="Upload">
#             </form>
#         </body>
#     </html>
# """

# @app.post("/uploads")
# async def upload_files(file: Annotated[UploadFile | None, File()]=None):
#     if not file:
#         return {
#             "message":"No file sent"
#         }
    
#     dir = "08_Form_handling/uploads"
#     save_path = f"{dir}/{file.filename}"
#     os.makedirs(dir,exist_ok=True)

#     with open(save_path, "wb") as buffer:
#         shutil.copyfileobj(file.file, buffer)

## Multiple Files upload
@app.get("/", response_class=HTMLResponse)
async def main():
    return """
    <html>
        <body>
            <h2>Multiple File Upload (bytes)</h2>
            <form action="/multiple-uploads" enctype="multipart/form-data" method="post">
                <input name="files" type="file" multiple="true">
                <input type="submit" value="Upload">
            </form>
        </body>
    </html>
"""

@app.post("/multiple-uploads")
async def upload_multiple_files(files: Annotated[List[UploadFile], File()]):
    return files