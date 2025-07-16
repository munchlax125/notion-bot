FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY .env .env
RUN echo "=== .env in container ===" && cat .env

COPY app/ ./app/

# 시작 스크립트 생성
RUN echo '#!/bin/bash\n\
echo "🚀 벡터 DB 업데이트 시작..."\n\
python app/update_vector_db.py\n\
echo "✅ 벡터 DB 업데이트 완료!"\n\
echo "🌐 웹서버 시작..."\n\
python app/chat_server.py' > /app/start.sh

RUN chmod +x /app/start.sh

EXPOSE 5000
CMD ["/app/start.sh"]