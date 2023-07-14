FROM python:3.9

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY Scraping.py .
COPY main.py .

VOLUME /app

CMD [ "python", "main.py" ]

