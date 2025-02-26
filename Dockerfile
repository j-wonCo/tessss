# 베이스 이미지로 Python 3.9 사용
FROM python:3.9-slim

# 작업 디렉토리 설정
WORKDIR /app

# 요구사항 파일 복사 및 설치
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 앱 코드 복사
COPY . .

# 80번 포트 노출
EXPOSE 80

# Gunicorn으로 Flask 앱 실행
CMD ["gunicorn", "--bind", "0.0.0.0:80", "app:app"]