from dotenv import load_dotenv
load_dotenv()

from flask import Flask, request, jsonify, render_template
from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from langchain_chroma import Chroma
from langchain.chains import RetrievalQA
import os

if not os.path.exists("chroma_db_notion"):
    from update_vector_db import setup_vector_db
    setup_vector_db()

app = Flask(__name__)
os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")
os.environ["CHROMA_TELEMETRY_ENABLED"] = "false"

vectorstore = Chroma(
    persist_directory="chroma_db_notion",
    embedding_function=OpenAIEmbeddings()
)
qa_chain = RetrievalQA.from_chain_type(
    llm=ChatOpenAI(model_name="gpt-3.5-turbo"),
    chain_type="stuff",
    retriever=vectorstore.as_retriever()
)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/ask", methods=["POST"])
def ask():
    data = request.json
    result = qa_chain.invoke(data["question"])
    return jsonify({"answer": result["result"]})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
