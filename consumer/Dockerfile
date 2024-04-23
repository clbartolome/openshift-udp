# Use Red Hat Universal Base Image (UBI) as a base image
FROM registry.access.redhat.com/ubi9/python-311

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY udp_consumer.py .

# Run udp_consumer.py when the container launches
CMD ["python", "udp_consumer.py"]