from crewai import Agent, Task, Crew
from pypdf import PdfReader

# =========================
# LOAD PDF
# =========================

pdf_path = "data/samplecase.pdf"

reader = PdfReader(pdf_path)

pdf_text = ""

for page in reader.pages:
    text = page.extract_text()
    if text:
        pdf_text += text

# =========================
# OLLAMA MODEL
# =========================

llm = "ollama/llama3:latest"

# =========================
# LEGAL AGENT
# =========================

legal_agent = Agent(
    role="Legal Research Specialist",
    goal="Analyze legal documents and identify risks",
    backstory="""
    You are an expert legal analyst specialized in:
    contracts, liabilities, compliance, obligations,
    legal risks and termination clauses.
    """,
    verbose=True,
    allow_delegation=False,
    llm=llm
)

# =========================
# TASK
# =========================

task = Task(
    description=f"""
    Analyze the following legal document carefully:

    {pdf_text}

    Identify:
    1. Important clauses
    2. Legal risks
    3. Financial liabilities
    4. Compliance issues
    5. Termination conditions
    6. Potential concerns

    Generate a professional legal analysis report.
    """,
    expected_output="Detailed legal analysis report",
    agent=legal_agent
)

# =========================
# CREW
# =========================

crew = Crew(
    agents=[legal_agent],
    tasks=[task],
    verbose=True
)

# =========================
# RUN
# =========================

result = crew.kickoff()

print("\nFINAL RESULT:\n")
print(result)