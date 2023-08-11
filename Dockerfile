FROM python:3.11

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . /app

EXPOSE 5000

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "5000"]

# Use this command to build your docker file " docker build -t fastapitrial ." where "fastapitrial" is the name of the container
# Use this command to see your docker images " docker image ls"
# Use this command to see which docker image is running " docker ps"
# Use this command to start the server inside the docker container "docker run -p 5000:5000 fastapitrial"
