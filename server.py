from fastapi import FastAPI, Request, UploadFile, File
from fastapi.templating import Jinja2Templates
import os
import sys
import shutil
import ocr

app = FastAPI()

templates = Jinja2Templates(directory="templates")


@app.get('/')
def home(request: Request):
    return templates.TemplateResponse('index.html',{"request": request})

@app.post('/extract_text')
async def perform_ocr(image: UploadFile = File(...)):
    filename=_save_file_to_disk(image, path='temp', save_as='temp')
    text= await ocr.read_image(filename)
    return {"filename": image.filename, "text":text}

def _save_file_to_disk(file, path='.', save_as='default'):

    extension = os.path.splitext(file.filename)[-1]
    temp_file_path=os.path.join(path, save_as + extension)
    
    with open(temp_file_path, 'wb') as buffer:
        shutil.copyfileobj(file.file, buffer)
    
    return temp_file_path 