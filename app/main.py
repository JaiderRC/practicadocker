from fastapi import FastAPI, Request
import json
import os

app = FastAPI()

@app.get("/")
async def root():
    return {
        "message": "Ejemplo de clase "
        "You can use this API to manage your notes."
    }
