FROM python:3.11-alpine
COPY . /demo-app
WORKDIR /demo-app
RUN pip install --no-cache-dir -r requirements.txt
EXPOSE 8000
#CMD ["python", "app.py"] #Simulate container crashing
CMD ["gunicorn", "-b", "0.0.0.0:8000", "app:app"]