from typing import Union
from fastapi import FastAPI
from retinaface import RetinaFace
app=FastAPI()
resp=RetinaFace.detect_faces("test.jpg")
resp=str(resp['face_1'])
@app.get("/")
async def detector():

    return str(resp)
