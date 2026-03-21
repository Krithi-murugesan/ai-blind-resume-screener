from crewai import Agent

def create_agents(llm):
  matcher = Agent(
        role='Technical Skill Matcher',
        goal=f'Compare the resume against this JD: {job_description}',
        backstory='You are a senior recruiter focusing on technical alignment only.',
        llm=llm
    )

  interviewer = Agent(
        role='Technical Interviewer',
        goal='Generate 5 deep dive interview questions based on the candidate’s skill gaps.',
        backstory='You identify what is missing in a profile and ask deep questions about it.',
        llm=llm
    )
  
  return matcher, interviewer
