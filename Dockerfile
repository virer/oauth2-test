FROM python:3.10

ENV FLASK_APP run.py

COPY requirements.txt /requirements.txt

RUN pip install --no-cache-dir -r /requirements.txt && rm -f /requirements.txt

COPY app/ /app/

WORKDIR /app

#CMD ["run:app", "flask shell"]
CMD ["python", "run.py"]