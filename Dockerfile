FROM python:3.12-rc-bullseye

EXPOSE 5000/tcp

#copy requirements.txt to the image
COPY ./requirements.txt /app/requirements.txt

WORKDIR /app

#switch working directory to /app
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

COPY . .

#ENV FLASK_APP=/app/index.py
CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]





