from dotenv import load_dotenv
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from langchain_core.prompts import PromptTemplate
from rag import get_context
import os

load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id="meta-llama/Llama-3.1-8B-Instruct",
    huggingfacehub_api_token=os.getenv("HF_TOKEN"),
    temperature=0.2,
    max_new_tokens=500
)

chat_model = ChatHuggingFace(llm=llm)

prompt = PromptTemplate(

    template="""You are PhishGuard, a cybersecurity threat-analysis assistant.

    Your task is DEFENSIVE ONLY.

    Analyze the already-existing message or URL provided by the user.

    Do not write, improve, or generate phishing messages.
    Do not provide instructions for carrying out phishing.

    Use the cybersecurity knowledge retrieved from the knowledge base
    to support your explanation.

    --------------------------------------------------
    USER INPUT
    --------------------------------------------------

    {message}

    --------------------------------------------------
    RULE-BASED ANALYSIS
    --------------------------------------------------

    Risk Score:
    {score}/100

    Detected Indicators:
    {indicators}

    --------------------------------------------------
    RETRIEVED CYBERSECURITY KNOWLEDGE
    --------------------------------------------------

    {context}

    --------------------------------------------------
    TASK
    --------------------------------------------------

    Analyze the input using both:

    1. The rule-based indicators
    2. The retrieved cybersecurity knowledge

    Respond using exactly these sections:

    Risk Assessment:
    Threat Category:
    Explanation:
    Warning Signs:
    Recommended Action:

    Important:

    - Treat the risk score as a heuristic.
    - Do not claim that the content is definitely malicious.
    - Do not reproduce or modify the suspicious message.
    - Use the retrieved knowledge as supporting context.
    - Give defensive and safe recommendations.
    """,

    input_variables=[
        "message",
        "score",
        "indicators",
        "context"
    ]
)

chain = prompt | chat_model


def analyze_with_llm(message, score, indicators):

    context = get_context(
        message,
        k=4
    )

    response = chain.invoke({
        "message": message,
        "score": score,
        "indicators": "\n".join(
            f"- {item}" for item in indicators
        ),
        "context" : context
    })

    return response.content




