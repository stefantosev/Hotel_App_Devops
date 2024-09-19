FROM python:3.12

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /Hotels

COPY requirements.txt /Hotels/

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

COPY . /Hotels/

EXPOSE 8080

CMD ["sh", "-c", "python manage.py migrate && python manage.py runserver 0.0.0.0:8080"]