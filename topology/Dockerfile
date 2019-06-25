FROM python:3.7.0-slim

WORKDIR /app

COPY Torus.py .
COPY requirements.txt .  

RUN pip install --upgrade pip
RUN pip install --trusted-host pypi.python.org -r requirements.txt

EXPOSE 5000 

CMD ["python","Torus.py"] 
