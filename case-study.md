# Case Study: Agentic AI Research Assistant

## 1. Abstract

An Agentic AI Research Assistant is a system that can plan research tasks, use tools to gather information, analyze findings, and produce a structured report. This case study explains its proposed design, workflow, benefits, and limitations.

## 2. Introduction

Research involves identifying reliable sources, collecting relevant information, comparing evidence, and preparing conclusions. Performing these tasks manually can take considerable time.

Agentic AI can help by dividing a research question into smaller tasks and carrying them out through an organized workflow. Depending on its configuration, an agent may use search tools, retrieve documents, summarize information, and revise its plan when necessary.

## 3. Problem Statement

Students and researchers may face several challenges:
- Finding relevant and trustworthy sources.
- Managing large amounts of information.
- Comparing findings from different sources.
- Identifying missing or conflicting evidence.
- Preparing structured reports with accurate references.

## 4. Objectives

- Explain how Agentic AI can support research.
- Describe planning and tool use in an AI agent.
- Propose a workflow for collecting and analyzing information.
- Identify security, accuracy, and ethical concerns.
- Define measurable criteria for evaluating the system.

## 5. Proposed System

The proposed Research Assistant accepts a question from a user and creates a plan to investigate it. It searches permitted information sources, collects relevant material, compares the findings, and drafts a report with references.

The user checks the report before relying on it. If sources are unavailable or evidence is insufficient, the system should communicate that limitation instead of inventing facts.

## 6. System Components

### 6.1 User Interface
Allows users to enter a research question and review the final report.

### 6.2 AI Agent
Coordinates the workflow, chooses the next task, and determines whether additional information is needed.

### 6.3 Language Model
Interprets the research question and assists with planning, classification, and summarization.

### 6.4 Search and Retrieval Tools
Retrieve information from approved websites, documents, or academic databases.

### 6.5 Analysis Module
Organizes findings by theme, compares claims, and identifies disagreements or information gaps.

### 6.6 Report Generator
Produces a structured report containing an introduction, findings, conclusion, and references.

### 6.7 Human Reviewer
Verifies important claims, checks citations, and approves the report for use.

## 7. Workflow

1. **Input:** The user enters a research question.
2. **Planning:** The agent divides the question into smaller research tasks.
3. **Retrieval:** Search tools gather relevant information from permitted sources.
4. **Filtering:** The system removes irrelevant material and records source details.
5. **Analysis:** The agent compares findings and identifies common themes or disagreements.
6. **Evaluation:** It checks whether the available evidence answers the question.
7. **Report generation:** The system prepares a structured draft with references.
8. **Human review:** The user checks accuracy and completeness before using the report.

## 8. Example Scenario

A student asks: "How is Agentic AI being used in education?"

The agent creates subtasks covering personalized learning, tutoring, administrative assistance, and assessment support. It searches approved sources, organizes the evidence into these categories, and drafts a report.

If two sources disagree, the system records the disagreement instead of treating one claim as automatically correct. The student verifies the sources before submitting the report.

This is a proposed example, not a claim that a working application has already been built or tested.

## 9. Suggested Technologies

- Python for application development.
- A large language model for language understanding and planning.
- Search APIs or document retrieval tools for gathering information.
- A document store or database for source material.
- A reporting library for generating structured output.
- Git and GitHub for version control and documentation.

The specific technologies depend on the implementation requirements and available access.

## 10. Advantages

- Reduces repetitive information-gathering work.
- Organizes research into manageable tasks.
- Helps compare findings across sources.
- Supports structured report preparation.
- Allows researchers to focus on interpretation and critical thinking.

## 11. Limitations and Risks

- Retrieved sources may be outdated or unreliable.
- The model may misinterpret evidence.
- Search tools may miss relevant publications.
- Citations may be incomplete or incorrect.
- Automated research can reproduce bias present in source material.
- Tool failures may interrupt the workflow.

## 12. Ethical and Security Considerations

The system should respect copyright and source access restrictions. It should not expose private information, and it should retain only the information needed for the task.

Claims should be traceable to sources. Important findings should be reviewed by a person, especially when they could influence academic, financial, medical, or other consequential decisions.

## 13. Evaluation Metrics

The system can be evaluated using:

- **Source relevance:** How closely retrieved sources address the question.
- **Factual accuracy:** Whether report claims agree with reliable evidence.
- **Citation accuracy:** Whether references support the associated claims.
- **Coverage:** Whether all important parts of the research question are addressed.
- **Completion time:** Time needed to produce a reviewed report.
- **User satisfaction:** Feedback from people using the system.

These metrics must be measured during actual testing; no performance results are assumed in this case study.

## 14. Future Scope

Future versions could support multilingual research, academic database integration, automatic reference formatting, document comparison, and collaboration between specialized agents. Any expanded automation should include source verification, permission controls, and human oversight.

## 15. Conclusion

An Agentic AI Research Assistant can organize research into a sequence of tasks involving planning, information retrieval, analysis, and report generation. It may improve efficiency, but its reliability depends on source quality, accurate citations, careful evaluation, and human review.

## 16. References for Further Reading

- IBM — Artificial Intelligence: https://www.ibm.com/think/topics/artificial-intelligence
- Google Cloud — What Are AI Agents?: https://cloud.google.com/discover/what-are-ai-agents
- Microsoft Learn — Azure AI Foundry: https://learn.microsoft.com/en-us/azure/ai-foundry/
