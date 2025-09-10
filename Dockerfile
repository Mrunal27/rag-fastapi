FROM python:3.12-slim

WORKDIR /app

COPY requirements.txt .

# Install base dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Install CPU-only torch from PyTorch's index
RUN pip install torch==2.1.0+cpu --index-url https://download.pytorch.org/whl/cpu

COPY . .

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]