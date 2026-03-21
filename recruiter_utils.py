from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter

def get_anonymized_text(pdf_path, llm):
    loader = PyPDFLoader(pdf_path)
    docs = loader.load()
    
    # Split for long resumes to avoid context window issues
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=3000, chunk_overlap=200)
    chunks = text_splitter.split_documents(docs)
    
    redacted_content = ""
    for chunk in chunks:
        prompt = f"REDACT all PII (Names, Emails, Phone, Address) from this text but keep professional skills: {chunk.page_content}"
        response = llm.invoke(prompt)
        redacted_content += str(response.content) + "\n"
    
    return redacted_content
