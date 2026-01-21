FROM python:3.11-slim

WORKDIR /dashboard

COPY ../requirements.txt .
RUN pip install flask

COPY . .

EXPOSE 5000
CMD ["python", "app.py"]
