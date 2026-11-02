
from agent import ResearchAgent


def main():

    print("\n*************************************")
    print("   AGENTIC AI RESEARCH ASSISTANT")
    print("*************************************")

    print("\nWelcome to your AI Research Assistant!")

    agent = ResearchAgent()

    while True:

        question = input(
            "\nEnter your research question "
            "(or type 'exit' to quit): "
        ).strip()

        if question.lower() == "exit":
            print("\nThank you for using the Research Assistant!")
            break

        if not question:
            print("Please enter a valid research question.")
            continue

        # Execute the agent's research workflow
        report = agent.research(question)

        # Save the generated report
        agent.save_research(report)

        print("\nResearch completed!")


if __name__ == "__main__":
    main()
