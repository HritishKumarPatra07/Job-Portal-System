from python:3.12-slim
workdir /app
copy requerment.txt .
run pip install  -r requerment.txt
copy . .
cmd ["uvicorn","main:app","--host","0.0.0.0","--port","8000"]