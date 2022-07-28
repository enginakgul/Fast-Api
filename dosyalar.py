
from typing import List, Union
from fastapi.responses import HTMLResponse
from fastapi import FastAPI,File , UploadFile
from pydantic import Field

"""
app = FastAPI()

@app.post("/files/")

async def create_file(file: bytes= File()):
    return {"file_size ": len(file)}

@app.post("/uploadfile/")
async def  create_upload_file(file: UploadFile):
    return {"filename" : file.filename}"""
    
app = FastAPI()

"""@app.post("/files/")
async def create_file(file: Union[bytes,None] = File(description="A file read as bytes")):
    if not file:
        return {"message":"No file sent"}
    else: 
        return {"file_size":len(file)}
    
@app.post("/uploadfile/")
async def create_update_file(file: Union[UploadFile,None]= File(description="A file read as UploadFile")):
    if not file:
        return {"message":"No upload file sent"}
    else: 
        return {"filename" : file.filename}"""



@app.post("/files/")
async def create_files(files: List[bytes] = File()):
    return {"files_sizes": [len(files) for file in files]}

@app.post("/uploadfiles/")
async def create_upload_files(files: List[UploadFile]):
    return {"filesname": [file.filename for file in files]}

@app.get("/")
async def main():
    content  = """
<body>
<form action="/files/" enctype="multipart/form-data" method="post">
<input name="files" type="file" multiple>
<input type="submit">
</form>
<form action="/uploadfiles/" enctype="multipart/form-data" method="post">
<input name="files" type="file" multiple>
<input type="submit">
</form>
</body>
    """
    return HTMLResponse(content = content)