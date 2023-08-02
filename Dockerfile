
FROM python:3.9-slim
WORKDIR /app
COPY . /app
# Installing the python dependencies
RUN pip install --no-cache-dir -r requirement.txt
EXPOSE 5001
# command to run my python web app when the container starts
CMD ["python", "run.py"]