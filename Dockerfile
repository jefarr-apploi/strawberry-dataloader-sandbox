# Use an official Python runtime as the parent image
FROM python:3.11-slim

# Set the working directory in the container to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Make port 8000 available to the world outside this container
#EXPOSE 8000

# Define environment variable for Gunicorn to bind on 0.0.0.0
#ENV BIND 0.0.0.0:8000

# Run app.py using gunicorn when the container launches
CMD ["gunicorn", "--worker-class", "gevent", "app:app", "-b", "0.0.0.0:8000"]
#CMD ["uvicorn", "app:asgi_app", "--host", "0.0.0.0", "--port", "8000", "--workers", "3"]
#CMD ["gunicorn", "--worker-class", "uvicorn.workers.UvicornWorker", "app:asgi_app", "-b", "0.0.0.0:8000", "--workers", "3"]
#CMD ["python", "app.py"]
