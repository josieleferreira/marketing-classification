FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 5000

ENV FLASK_APP=app.py
ENV FLASK_ENV=development

CMD ["python", "-m", "flask", "run", "--host=0.0.0.0", "--port=5000", "--reload"]


# CMD ["flask", "run", "--host=0.0.0.0", "--port=5000", "--reload"]