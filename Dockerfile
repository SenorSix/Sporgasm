# Use an official Python runtime
FROM python:3.10.12

# Set working directory
WORKDIR /app

# Copy current directory contents into /app
COPY . .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Make port 5000 available
EXPOSE 5000

#Run the app
CMD ["python3", "run.py"]
