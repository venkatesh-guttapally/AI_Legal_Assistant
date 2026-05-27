from crewai import Agent, Task, Crew
import ollama

# =========================
# LEGAL ANALYSIS FUNCTION
# =========================

def analyze_legal_document(pdf_text):

    # =========================
    # LEGAL AGENT
    # =========================

    legal_agent = Agent(
        role="Legal Research Specialist",

        goal="""
        Analyze legal documents and identify:
        - risks
        - liabilities
        - obligations
        - compliance issues
        """,

        backstory="""
        You are an expert legal analyst specialized in:
        contracts,
        liabilities,
        compliance,
        obligations,
        legal risks,
        and termination clauses.
        """,

        verbose=True,

        allow_delegation=False,

        llm="ollama/llama3"
    )

    # =========================
    # TASK
    # =========================

    legal_task = Task(

        description=f"""
        Analyze the following legal document carefully.

        LEGAL DOCUMENT:
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

        expected_output="""
        A detailed legal analysis report with:
        - key clauses
        - risks
        - liabilities
        - compliance concerns
        - summary
        """,

        agent=legal_agent
    )

    # =========================
    # CREW
    # =========================

    crew = Crew(

        agents=[legal_agent],

        tasks=[legal_task],

        verbose=True
    )

    # =========================
    # EXECUTE
    # =========================

    result = crew.kickoff()

    #return result
    
    return str(result)