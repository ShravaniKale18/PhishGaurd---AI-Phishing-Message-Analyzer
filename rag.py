import os

from langchain_community.document_loaders import DirectoryLoader, TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS


# PATHS

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

KNOWLEDGE_DIR = os.path.join(BASE_DIR, "knowledge")
VECTORSTORE_DIR = os.path.join(BASE_DIR, "vectorstore")


# EMBEDDING MODEL

embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)


# CREATE VECTORSTORE

def create_vectorstore():

    print("\nCreating FAISS vectorstore...")
    print("Knowledge directory:", KNOWLEDGE_DIR)
    print("Vectorstore directory:", VECTORSTORE_DIR)

    # Create vectorstore folder
    os.makedirs(VECTORSTORE_DIR, exist_ok=True)

    # Check folder
    if not os.path.isdir(VECTORSTORE_DIR):
        raise RuntimeError(
            f"Could not create vectorstore folder:\n{VECTORSTORE_DIR}"
        )

    print("Vectorstore folder exists.")

    # Load knowledge files

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

    print(f"Loaded {len(documents)} knowledge files.")

    # Split documents

    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=700,
        chunk_overlap=100
    )

    chunks = text_splitter.split_documents(documents)

    print(f"Created {len(chunks)} chunks.")

    # Create FAISS database

    vectorstore = FAISS.from_documents(
        chunks,
        embeddings
    )

    # Make sure directory still exists
    os.makedirs(VECTORSTORE_DIR, exist_ok=True)

    # Save FAISS
    vectorstore.save_local(
        folder_path=VECTORSTORE_DIR,
        index_name="index"
    )

    print("FAISS vectorstore created successfully!")

    print("Files created:")

    for file in os.listdir(VECTORSTORE_DIR):
        print(" -", file)

    return vectorstore


# LOAD VECTORSTORE

def load_vectorstore():

    index_file = os.path.join(
        VECTORSTORE_DIR,
        "index.faiss"
    )

    pickle_file = os.path.join(
        VECTORSTORE_DIR,
        "index.pkl"
    )

    # If files don't exist, create the database
    if not os.path.exists(index_file) or not os.path.exists(pickle_file):

        print("FAISS vectorstore not found.")
        print("Creating a new vectorstore...")

        return create_vectorstore()

    print("Loading existing FAISS vectorstore...")

    vectorstore = FAISS.load_local(
        VECTORSTORE_DIR,
        embeddings,
        allow_dangerous_deserialization=True
    )

    return vectorstore


# RETRIEVE KNOWLEDGE

def retrieve_knowledge(query, k=4):

    vectorstore = load_vectorstore()

    documents = vectorstore.similarity_search(
        query,
        k=k
    )

    return documents


# GET CONTEXT FOR LLM

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