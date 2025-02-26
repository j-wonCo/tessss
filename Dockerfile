# Python 공식 이미지 사용 (최신 버전)
FROM python:3.11-slim

# 작업 디렉토리 설정
WORKDIR /code

# 필요한 파일 복사
COPY requirements.txt .

# 의존성 설치
RUN pip install --no-cache-dir -r requirements.txt
COPY . .

EXPOSE 50505
# Flask 서버 실행
ENTRYPOINT ["gunicorn", "app:app"]