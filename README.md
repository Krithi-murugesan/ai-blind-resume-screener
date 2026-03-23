# 🕵️‍♂️ AI Blind Resume Screener

Multi-Agent Recruitment Pipeline with CrewAI, LangChain, and Openai

This project solves the problem of unconscious bias in recruitment. It uses a specialized AI "Crew" to anonymize resumes—stripping away PII (Personally Identifiable Information)—and then evaluates the candidate's technical skills against a dynamic Job Description (JD).

## 🚀 Key Features

PII Redaction: Automatically strips names, emails, and locations using LangChain's recursive text splitting to handle large documents.

Multi-Agent Orchestration: Powered by CrewAI, featuring a Technical Recruiter Agent for skill matching and an Interviewer Agent for gap analysis.

Cost-Efficient Inference: Utilizes Openai for high-speed, low-cost LLM processing.

Serverless Persistence: Saves all screening reports and interview questions into Amazon DynamoDB.

## 🏗️ Architecture

Ingestion: Python script takes a PDF and a JD as dynamic command-line inputs.

Processing: * LangChain splits the PDF into chunks.

Openai Chat Model redacts sensitive information.

Analysis: CrewAI agents collaborate to score the candidate and generate 5 technical questions.

Storage: The final analysis is pushed to an AWS DynamoDB table.

## 🛠️ Tech Stack

Orchestration: CrewAI

Framework: LangChain

Cloud Provider: AWS (SES, DynamoDB, IAM)

LLM: Openai Chat Model

Language: Python 3.11+

## 📋 Prerequisites

An AWS IAM User with AmazonDynamoDBFullAccess and AmazonBedrockFullAccess.

A DynamoDB table named CandidateScores with CandidateID as the Partition Key.

## ⚙️ Setup & Installation
Clone the Repository:

Bash
git clone https://github.com/your-username/blind-resume-screener.git
cd blind-resume-screener

Install Dependencies:

Bash

pip install crewai langchain-aws langchain-community boto3 pypdf

Environment Variables:
Create a .env file or export your credentials:

Bash
export AWS_ACCESS_KEY_ID='your_key'

export AWS_SECRET_ACCESS_KEY='your_secret'

export AWS_DEFAULT_REGION='us-east-1'

## 🚀 Usage

The script accepts the resume path and the Job Description as dynamic arguments:

Bash
python main.py "resumes/john_doe.pdf" "We are looking for a Senior Python Developer with 5+ years of AWS experience and Expertise in AI Orchestration."
## 🤖 Agent Breakdown

Technical Skill Matcher: Analyzes the redacted resume for technical stack alignment. It generates a score from 0-100.

Technical Interviewer: Identifies missing skills in the candidate's profile and creates targeted questions to verify their depth during an interview.

## 💡 Future Enhancements

[ ] Frontend: Add a Streamlit dashboard to view screening results.

[ ] Automated Trigger: Deploy as a Dockerized AWS Lambda triggered by S3 uploads.

[ ] Multi-Model Support: Implement A/B testing between Claude 3 and Llama 3 via Bedrock.
