**API 키 준비**

```bash
# .env 파일 생성
OPENAI_API_KEY=your-openai-api-key
NOTION_API_KEY=your-notion-api-key
NOTION_DATABASE_ID=your-notion-database-id

```

### 실행 단계

```bash
# 1. 의존성 설치
pip install -r requirements.txt

# 2. 벡터 DB 초기 생성 (최초 실행 또는 노션 업데이트 시)
python app/update_vector_db.py

# 3. 웹 서버 실행
python app/chat_server.py

# 또는 Docker로 실행
docker build -t notion-chatbot .
docker run -p 5000:5000 notion-chatbot

```

https://github.com/munchlax125/notion-bot/blob/main/requirements.txt

### 실행 결과

**성공적인 실행 시:**

- 웹 브라우저에서 `http://localhost:5000` 접속
- "업무 매뉴얼 챗봇" 인터페이스 로딩
- 질문 입력 후 실시간 AI 답변 수신
