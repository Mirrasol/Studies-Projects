import os

from dotenv import load_dotenv
from fastapi import FastAPI
from fastapi.responses import FileResponse

load_dotenv()

app = FastAPI()
path = os.getenv('PAGE')


@app.get('/')
async def webpage():
    return FileResponse(path)
