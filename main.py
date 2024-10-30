import json
from  fastapi import FastAPI
import random


app = FastAPI()

@app.get('/')

async def root():
    return {'example': 'this is a trail api ', 'data': 0 }