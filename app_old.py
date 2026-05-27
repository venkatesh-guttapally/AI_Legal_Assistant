from crewai import Agent, Task, Crew
from crewai_tools import PDFSearchTool
from dotenv import load_dotenv
import os

load_dotenv()

# PDF Search Tool
pdf_tool = PDFSearchTool(
    pdf='data/samplecase.pdf'
)

# Legal Research Agent
legal_researcher = Agent(
    role="Legal Research Specialist",
    goal="Analyze legal documents and identify important legal clauses",
    backstory="""
    You are an expert legal researcher with deep understanding
    of contracts, agreements, compliance and legal terminology.
    """,
    verbose=True,
    allow_delegation=False,
    tools=[pdf_tool]
)

# Task
research_task = Task(
    description="""
    Analyze the uploaded legal contract.
    
    Find:
    1. Important clauses
    2. Risks
    3. Obligations
    4. Termination conditions
    5. Compliance issues

    Generate a detailed legal summary.
    """,
    expected_output="Detailed legal analysis report",
    agent=legal_researcher
)

# Crew
crew = Crew(
    agents=[legal_researcher],
    tasks=[research_task],
    verbose=True
)

# Run
result = crew.kickoff()

print("\nFINAL RESULT:\n")
print(result)