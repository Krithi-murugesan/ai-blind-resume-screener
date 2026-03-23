
import os
import sys
import boto3
from dotenv import load_dotenv
from crewai import Crew, Process
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_openai import ChatOpenAI  
from aws_helpers import get_llm, save_to_dynamodb, send_ses_email
from recruiter_utils import get_anonymized_text
from agents import create_agents
from tasks import create_tasks

load_dotenv()

def main():
    if len(sys.argv) < 3:
        print("Usage: python main.py <path_to_resume.pdf> <'Job Description'>")
        return

    resume_path = sys.argv[1]
    job_description = sys.argv[2]
    candidate_id = os.path.basename(resume_path).replace(".pdf", "")

    # 1. Initialize LLM (AWS Bedrock)
    llm = get_llm()

    # 2. Anonymize Resume (LangChain)
    print("Step 1: Redacting PII...")
    redacted_text = get_anonymized_text(resume_path, llm)

    # 3. Setup CrewAI
    print("Step 2: Starting CrewAI Analysis...")
    matcher, interviewer = create_agents(llm)
    tasks = create_tasks(matcher, interviewer, redacted_text, job_description)

    crew = Crew(
        agents=[matcher, interviewer],
        tasks=tasks,
        process=Process.sequential
    )

    # 4. Execute
    result = crew.kickoff()

    # 5. Save to DynamoDB
    print("Step 3: Saving to AWS...")
    save_to_dynamodb('CandidateScores', {
        'CandidateID': candidate_id,
        'Report': str(result)
    })

    print(f"\n✅ Screening complete for {candidate_id}")
    print(result)
    
    # 6: Send SES   Email
    print("✉️ Step 4: Sending SES Notification...")
    send_ses_email(SENDER, RECEIVER, f"Screening Complete: {candidate_id}", str(result))

    print(f"\n✅ DONE! Process complete for {candidate_id}.")
    
if __name__ == "__main__":
    
    main()
