FROM python:3.9-slim

WORKDIR /app

# Copy the Flask server script and Utils.py file
COPY MainScores.py /app/MainScores.py
COPY Utils.py /app/Utils.py

# Copy the requirements.txt file
COPY requirements.txt /app/requirements.txt

# Install dependencies
RUN pip install -r requirements.txt

# Copy the scores.txt file
COPY Scores.txt /app/Scores.txt

# Set the Flask script as the entry point
CMD ["python", "MainScores.py"]
