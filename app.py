from crewai import Agent, Task, Crew

# ==================================================
# LEGAL AI ANALYSIS FUNCTION
# ==================================================

def analyze_legal_document(pdf_text):

    # ==================================================
    # AGENT 1 — ANALYSIS AGENT
    # ==================================================

    analysis_agent = Agent(

        role="Legal Analysis Specialist",

        goal="""
        Understand the legal document structure,
        identify clauses, obligations, and key topics.
        """,

        backstory="""
        You are an expert legal analyst specialized in:
        contracts,
        agreements,
        obligations,
        clause interpretation,
        and legal document understanding.
        """,

        verbose=True,

        allow_delegation=False,

        llm="ollama/llama3"
    )

    # ==================================================
    # AGENT 2 — RISK AGENT
    # ==================================================

    risk_agent = Agent(

        role="Legal Risk Analyst",

        goal="""
        Detect legal risks, liabilities,
        financial exposure, and dangerous clauses.
        """,

        backstory="""
        You specialize in:
        legal liabilities,
        financial exposure,
        indemnity risks,
        penalty clauses,
        and contractual dangers.
        """,

        verbose=True,

        allow_delegation=False,

        llm="ollama/llama3"
    )

    # ==================================================
    # AGENT 3 — COMPLIANCE AGENT
    # ==================================================

    compliance_agent = Agent(

        role="Compliance Officer",

        goal="""
        Identify compliance concerns,
        governance issues,
        and regulatory violations.
        """,

        backstory="""
        You are an expert in:
        compliance analysis,
        regulations,
        governance,
        policy adherence,
        and legal standards.
        """,

        verbose=True,

        allow_delegation=False,

        llm="ollama/llama3"
    )

    # ==================================================
    # AGENT 4 — DRAFTING AGENT
    # ==================================================

    drafting_agent = Agent(

        role="Legal Drafting Specialist",

        goal="""
        Draft professional legal observations,
        recommendations, and suggested actions.
        """,

        backstory="""
        You are an expert legal drafting assistant
        specialized in:
        recommendations,
        legal observations,
        contract improvements,
        and professional legal writing.
        """,

        verbose=True,

        allow_delegation=False,

        llm="ollama/llama3"
    )

    # ==================================================
    # AGENT 5 — SUMMARY AGENT
    # ==================================================

    summary_agent = Agent(

        role="Executive Legal Summary Specialist",

        goal="""
        Generate concise and professional
        executive summaries of legal documents.
        """,

        backstory="""
        You specialize in simplifying complex
        legal documents into concise,
        professional summaries understandable
        by clients and executives.
        """,

        verbose=True,

        allow_delegation=False,

        llm="ollama/llama3"
    )

    # ==================================================
    # TASK 1 — ANALYSIS TASK
    # ==================================================

    analysis_task = Task(

        description=f"""
        Analyze the following legal document carefully.

        LEGAL DOCUMENT:
        {pdf_text}

        Identify:
        1. Important clauses
        2. Contract structure
        3. Key obligations
        4. Termination conditions
        5. Main legal topics

        Generate a professional legal analysis report.
        """,

        expected_output="""
        Detailed legal document understanding report
        including clauses, obligations,
        structure, and legal interpretation.
        """,

        agent=analysis_agent
    )

    # ==================================================
    # TASK 2 — RISK TASK
    # ==================================================

    risk_task = Task(

        description="""
        Based on the legal analysis report,
        identify:

        1. Legal liabilities
        2. Financial risks
        3. Penalty clauses
        4. Indemnity risks
        5. Dangerous contractual terms
        6. Potential legal exposure

        Generate a detailed legal risk report.
        """,

        expected_output="""
        Comprehensive legal risk analysis report
        highlighting liabilities,
        penalties,
        and contractual dangers.
        """,

        agent=risk_agent,

        context=[analysis_task]
    )

    # ==================================================
    # TASK 3 — COMPLIANCE TASK
    # ==================================================

    compliance_task = Task(

        description="""
        Based on the legal analysis and risk analysis,
        identify:

        1. Compliance concerns
        2. Governance issues
        3. Regulatory risks
        4. Policy violations
        5. Legal compliance gaps

        Generate a compliance analysis report.
        """,

        expected_output="""
        Professional compliance analysis report
        covering governance,
        regulations,
        and compliance risks.
        """,

        agent=compliance_agent,

        context=[analysis_task, risk_task]
    )

    # ==================================================
    # TASK 4 — DRAFTING TASK
    # ==================================================

    drafting_task = Task(

        description="""
        Based on the analysis,
        risk findings,
        and compliance report,

        draft:

        1. Legal recommendations
        2. Suggested improvements
        3. Risk mitigation suggestions
        4. Professional legal observations
        5. Suggested corrective actions

        Generate a professional legal recommendation document.
        """,

        expected_output="""
        Professional legal drafting report
        including recommendations,
        observations,
        and corrective suggestions.
        """,

        agent=drafting_agent,

        context=[
            analysis_task,
            risk_task,
            compliance_task
        ]
    )

    # ==================================================
    # TASK 5 — SUMMARY TASK
    # ==================================================

    summary_task = Task(

        description="""
        Based on all previous reports,

        generate:

        1. Executive summary
        2. Key findings
        3. Major risks
        4. Compliance overview
        5. Final observations

        Create a concise professional summary.
        """,

        expected_output="""
        Concise executive-level legal summary report.
        """,

        agent=summary_agent,

        context=[
            analysis_task,
            risk_task,
            compliance_task,
            drafting_task
        ]
    )

    # ==================================================
    # CREW
    # ==================================================

    crew = Crew(

        agents=[

            analysis_agent,
            risk_agent,
            compliance_agent,
            drafting_agent,
            summary_agent
        ],

        tasks=[

            analysis_task,
            risk_task,
            compliance_task,
            drafting_task,
            summary_task
        ],

        verbose=True
    )

    # ==================================================
    # EXECUTE CREW
    # ==================================================

    result = crew.kickoff()

    return str(result)