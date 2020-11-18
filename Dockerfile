FROM python:3.7
WORKDIR /application
RUN pip install Flask Flask-SQLAlchemy Flask-WTF PyMySQL WTForms gunicorn
COPY . .
ENV 'DB_URI'='mysql+pymysql://root:root@35.246.12.217/board'
ENV 'SECRET_KEY'='its a secret'
RUN python3 create.py
EXPOSE 5000
ENTRYPOINT ["python", "app.py"]
