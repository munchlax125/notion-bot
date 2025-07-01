# update_vector_db.py

import os
import shutil
from langchain_community.document_loaders import NotionDBLoader
from langchain_openai import OpenAIEmbeddings
from langchain_chroma import Chroma
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores.utils import filter_complex_metadata



from dotenv import load_dotenv

load_dotenv()

NOTION_API_KEY = os.getenv("NOTION_API_KEY")
NOTION_DATABASE_ID = os.getenv("NOTION_DATABASE_ID")
PERSIST_DIRECTORY = "chroma_db_notion"

def setup_vector_db():
    print("📥 Notion 데이터 불러오는 중...")
    loader = NotionDBLoader(
        integration_token=NOTION_API_KEY,
        database_id=NOTION_DATABASE_ID,
        request_timeout_sec=30,
    )
    docs = loader.load()
    docs = filter_complex_metadata(docs)
    print(f"✅ 문서 수: {len(docs)}")

    if not docs:
        print("❌ 문서 없음! API 키, DB ID, 공유 설정 확인 필요")
        return None

    print("🧩 문서 분할 및 임베딩 중...")
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=100)
    splits = text_splitter.split_documents(docs)

    if os.path.exists(PERSIST_DIRECTORY):
        shutil.rmtree(PERSIST_DIRECTORY)

    embeddings = OpenAIEmbeddings()

    vectorstore = Chroma.from_documents(
        documents=splits,
        embedding=embeddings,
        persist_directory=PERSIST_DIRECTORY
    )
    print("✅ 벡터 DB 생성 완료!")
    return vectorstore

if __name__ == "__main__":
    setup_vector_db()
