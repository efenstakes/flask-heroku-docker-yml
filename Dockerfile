
FROM python:3.7-alpine 

WORKDIR /app

COPY . .

RUN pip install -r requirements.txt 

# EXPOSE 5000

# ENV PORT 5000

# ENTRYPOINT gunicorn run:app --bind :$PORT
CMD gunicorn run:app --bind 0.0.0.0:$PORT
# CMD python run.py