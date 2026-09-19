import os

from langchain_community.document_loaders import DirectoryLoader, TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS


# PATHS

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

KNOWLEDGE_DIR = os.path.join(
    BASE_DIR,
    "knowledge"
)

VECTORSTORE_DIR = os.path.join(
    BASE_DIR,
    "vectorstore"
)


# EMBEDDING MODEL

embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)


# CREATE VECTOR DATABASE

def create_vectorstore():

    loader = DirectoryLoader(
        KNOWLEDGE_DIR,
        glob="*.txt",
        loader_cls=TextLoader,
        loader_kwargs={
            "encoding": "utf-8"
        }
    )

    documents = loader.load()

    if not documents:
        raise ValueError(
            "No knowledge files found in the knowledge folder."
        )

    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=700,
        chunk_overlap=100
    )

    chunks = text_splitter.split_documents(
        documents
    )

    vectorstore = FAISS.from_documents(
        chunks,
        embeddings
    )

    vectorstore.save_local(
        VECTORSTORE_DIR
    )

    return vectorstore


# LOAD VECTOR DATABASE

def load_vectorstore():

    if not os.path.exists(VECTORSTORE_DIR):

        return create_vectorstore()

    vectorstore = FAISS.load_local(
        VECTORSTORE_DIR,
        embeddings,
        allow_dangerous_deserialization=True
    )

    return vectorstore


# RETRIEVE RELEVANT KNOWLEDGE

def retrieve_knowledge(query, k=4):

    vectorstore = load_vectorstore()

    documents = vectorstore.similarity_search(
        query,
        k=k
    )

    return documents


# FORMAT RETRIEVED KNOWLEDGE

def get_context(query, k=4):

    documents = retrieve_knowledge(
        query,
        k=k
    )

    if not documents:
        return "No relevant cybersecurity knowledge was found."

    context = []

    for i, document in enumerate(documents, start=1):

        context.append(
            f"[Knowledge Source {i}]\n"
            f"{document.page_content}"
        )

    return "\n\n".join(context)