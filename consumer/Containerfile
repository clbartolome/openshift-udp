# Use Red Hat Universal Base Image (UBI) as a base image
FROM registry.access.redhat.com/ubi9/python-3.11

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed dependencies specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Run udp_consumer.py when the container launches
CMD ["python", "udp_consumer.py"]