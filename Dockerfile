FROM python:3.12-slim

WORKDIR /app

# Mengatur variabel lingkungan
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Menginstal dependensi
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Menyalin proyek
COPY . /app/

# Mengekspos port aplikasi Django
EXPOSE 8000

# Menjalankan server
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "gameapi.wsgi:application"]