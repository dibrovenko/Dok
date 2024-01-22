from fastapi import FastAPI

from main_screen import test_fullpage_screenshot

app = FastAPI()


@app.get("/")
def read_root():
    #test_fullpage_screenshot("https://tproger.ru", "tproger.png")
    #test_fullpage_screenshot("https://stackoverflow.com", "stackoverflow.png")

    return {"Hello nvhv": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}




"""FROM python:3.12

RUN apt-get update
RUN apt-get install -y gconf-service libasound2 libatk1.0-0 libcairo2 libcups2 libfontconfig1 libgdk-pixbuf2.0-0 libgtk-3-0 libnspr4 libpango-1.0-0 libxss1 fonts-liberation libappindicator1 libnss3 lsb-release xdg-utils

#download and install chrome
RUN wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
RUN dpkg -i google-chrome-stable_current_amd64.deb; apt-get -fy install

#install python dependencies
COPY requirements.txt requirements.txt
RUN pip install -r ./requirements.txt

#some envs
ENV APP_HOME /app
ENV PORT 5000

#set workspace
WORKDIR ${APP_HOME}

#copy local files
COPY . .

CMD gunicorn main:app --workers 1 --worker-class uvicorn.workers.UvicornWorker --bind=0.0.0.0:8000

"""