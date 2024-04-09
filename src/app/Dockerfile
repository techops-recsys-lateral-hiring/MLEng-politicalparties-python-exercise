# Dockerfile for demo
FROM python:3.9

# Set a directory for the app
WORKDIR /usr/src/app

# Copy the requirements file
COPY ./app/requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the current directory contents into the container
COPY ./app .

# Command to run the application
CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]
