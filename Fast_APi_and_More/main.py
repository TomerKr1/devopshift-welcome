from log import setup_logging
from fastapi import FastAPI


# logger = setup_logging()

app=FastAPI()



@app.get("/")
def hello_world():
    "This is our main function"
    return {"Rsult":3213}


