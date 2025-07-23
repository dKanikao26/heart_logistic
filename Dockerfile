# Start from an official Python image, matching your development version
FROM python:3.11-slim

# Set the working directory
WORKDIR /app

# Copy only requirements first for efficient caching
COPY requirements.txt .

# Install dependencies
RUN pip install --upgrade pip && pip install --no-cache-dir -r requirements.txt

# Copy everything else into the image
COPY . .

# Expose necessary ports (8000 for FastAPI, 8501 for Streamlit)
EXPOSE 8000
EXPOSE 8501

# Choose which app to run by default—FastAPI via Uvicorn, or Streamlit
# To run FastAPI backend:
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]

# To run Streamlit frontend, swap to this line:
# CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]
