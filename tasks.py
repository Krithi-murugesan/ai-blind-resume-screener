from crewai import Task

def create_tasks(matcher_agent, interviewer_agent, anonymized_resume, job_desc):

task_match = Task(
        description=f"Analyze this redacted resume: {anonymized_resume}",
        agent=matcher,
        expected_output="A match score (0-100) and a summary of missing vs matching skills."
    )

    task_questions = Task(
        description="Write 5 technical questions to test the missing skills identified.",
        agent=interviewer,
        expected_output="A list of 5 targeted interview questions."
    )
return [task_match, task_questions]
