# Use an official Python runtime as a base image
FROM python:3.9.7-buster

# Set environment variables
ENV PYTHONUNBUFFERED 1

# Set working directory
WORKDIR /home/ikechukwu-nwamah/Desktop/vegil/veegil/

# Copy the current directory contents into the container at /home/ikechukwu-nwamah/Desktop/vegil/veegil/
COPY . /home/ikechukwu-nwamah/Desktop/vegil/veegil/

# Install system dependencies
RUN apt-get update && \
    apt-get install -y netcat gcc && \
    rm -rf /var/lib/apt/lists/*

# Upgrade pip
RUN pip install --upgrade pip

# Install Python dependencies
COPY requirements.txt /home/ikechukwu-nwamah/Desktop/vegil/veegil/
RUN pip install -r requirements.txt

# Install Gunicorn
RUN pip install gunicorn

# Expose port 5000
EXPOSE 5000

# Define the command to run the application
CMD ["gunicorn", "--bind", ":5000", "veegil.wsgi:application"]
