# 업무 매뉴얼 챗봇

## 실행 방법

### 1. 환경 설정
`.env` 파일에 API 키 설정:
```env
OPENAI_API_KEY=your-openai-api-key
NOTION_API_KEY=your-notion-api-key
NOTION_DATABASE_ID=your-notion-database-id
```

### 2. 실행
```bash
# 컨테이너 실행
docker-compose up -d

# 벡터 DB 생성 (최초 실행 또는 노션 업데이트 시)
docker-compose exec chatbot python app/update_vector_db.py

# 브라우저에서 http://localhost:5000 접속
```

### 3. 관리 명령어
```bash
# 컨테이너 중지
docker-compose down

# 노션 내용 업데이트 시
docker-compose exec chatbot python app/update_vector_db.py
```