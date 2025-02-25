# Python 공식 이미지 사용 (최신 버전)
FROM python:3.11-slim

# 작업 디렉토리 설정
WORKDIR /app

# 필요한 파일 복사
COPY requirements.txt .
COPY app.py .

# 의존성 설치
RUN pip install --no-cache-dir -r requirements.txt

# Flask 앱 실행 환경 변수 설정
ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0
ENV FLASK_RUN_PORT=80  # 포트를 80으로 설정

# Flask 서버 실행
CMD ["gunicorn", "--bind", "0.0.0.0:80", "app:app"]