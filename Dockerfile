
FROM python:3.9-slim-buster
ADD run.py /
COPY . /app
WORKDIR /app
# Installing the python dependencies
RUN pip install --no-cache-dir -r requirement.txt
EXPOSE 5003
# command to run my python web app when the container starts
CMD ["python3", "./run.py"]
