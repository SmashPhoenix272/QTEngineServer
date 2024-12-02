# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Clone the QTEngine repository
RUN git clone https://github.com/SmashPhoenix272/QTEngine.git QTEngine

# Install QTEngine requirements
RUN pip install --no-cache-dir -r QTEngine/requirements.txt

# Install QTEngineServer requirements
RUN pip install --no-cache-dir -r requirements.txt

# Make port 2210 available to the world outside this container
EXPOSE 2210

# Define environment variable
ENV NAME QTEngineServer

# Run QTEngineServer.py when the container launches
CMD ["python", "QTEngineServer.py"]
