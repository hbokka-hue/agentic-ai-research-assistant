
from tools import search_knowledge_base, save_report


class ResearchAgent:
    """A goal-oriented research agent."""

    def __init__(self):
        self.name = "AI Research Assistant"

    def create_plan(self, question):
        """Create a research plan based on the user's question."""

        print("\n[AGENT] Analyzing your research question...")

        plan = [
            "Understand the research objective",
            "Identify important research keywords",
            "Select the knowledge retrieval tool",
            "Collect relevant information",
            "Analyze the retrieved information",
            "Generate a research report"
        ]

        for number, task in enumerate(plan, start=1):
            print(f"{number}. {task}")

        return plan

    def select_tool(self, question):
        """Choose the research tool based on the question."""

        print("\n[AGENT] Selecting an appropriate tool...")

        # The current prototype uses a local knowledge-base search.
        return search_knowledge_base

    def research(self, question):
        """Execute the research workflow."""

        print("\n===================================")
        print("       AGENTIC AI RESEARCH")
        print("===================================")

        # Step 1: Planning
        self.create_plan(question)

        # Step 2: Tool selection
        research_tool = self.select_tool(question)

        # Step 3: Information retrieval
        print("\n[AGENT] Searching the knowledge base...")

        results = research_tool(question)

        # Step 4: Analyze the results
        print("[AGENT] Analyzing research findings...")

        if not results:
            print("[AGENT] No matching information found.")

            report = f"""# Research Report

## Research Question
{question}

## Result
No matching information was found in the local knowledge base.

## Recommendation
Add relevant research material to knowledge_base.json
or connect an additional approved information source.
"""
            return report

        # Step 5: Generate report
        report = f"""# Agentic AI Research Report

## Research Question
{question}

## Research Plan
1. Understand the research objective.
2. Identify relevant keywords.
3. Search the knowledge base.
4. Retrieve relevant information.
5. Analyze the findings.
6. Generate the report.

## Research Findings
"""

        for number, document in enumerate(results, start=1):
            report += f"""
### {number}. {document['title']}

**Topic:** {document['topic']}

**Findings:** {document['content']}

**Source label:** {document['source']}

"""

        report += """
## Analysis

The retrieved documents provide information related to the
research question. The findings can be used as a starting
point for further investigation.

The retrieved material comes from a local demonstration
knowledge base. Its source labels are not independently
verified publications.

## Conclusion

The research assistant successfully executed its local
research workflow by planning the task, selecting a search
tool, retrieving information, and generating a report.

## Limitations

This prototype uses keyword-based retrieval and a fixed
local knowledge base. It does not currently use a live
internet search engine or a large language model.
"""

        print("[AGENT] Research report generated successfully!")

        return report

    def save_research(self, report):
        """Save the generated report."""

        file_path = save_report(report)

        print("\n[AGENT] Report saved successfully!")
        print(f"[AGENT] Location: {file_path}")

        return file_path
