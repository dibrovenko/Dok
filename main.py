from fastapi import FastAPI

from main_screen import test_fullpage_screenshot

app = FastAPI()


@app.get("/")
def read_root():
    test_fullpage_screenshot("https://tproger.ru", "tproger.png")
    #test_fullpage_screenshot("https://stackoverflow.com", "stackoverflow.png")

    return {"Hello nvhv": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}




"""FROM python:3.12

RUN mkdir /fastapi_app

WORKDIR / fastapi_app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

CMD gunicorn main:app --workers 1 --worker-class uvicorn.workers.UvicornWorker --bind=0.0.0.0:8000"""