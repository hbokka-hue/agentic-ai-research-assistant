
import json
import os


def load_knowledge_base():
    """Load research information from the local JSON database."""

    file_path = os.path.join(
        os.path.dirname(__file__),
        "knowledge_base.json"
    )

    with open(file_path, "r", encoding="utf-8") as file:
        return json.load(file)


def search_knowledge_base(query):
    """Search the knowledge base using keywords."""

    documents = load_knowledge_base()

    keywords = query.lower().split()
    results = []

    for document in documents:
        searchable_text = (
            document["title"] + " " +
            document["topic"] + " " +
            document["content"]
        ).lower()

        score = sum(
            1 for word in keywords
            if word in searchable_text
        )

        if score > 0:
            results.append((score, document))

    results.sort(key=lambda item: item[0], reverse=True)

    return [document for score, document in results]


def save_report(content, filename="research_report.md"):
    """Save the generated research report."""

    reports_folder = os.path.join(
        os.path.dirname(__file__),
        "reports"
    )

    os.makedirs(reports_folder, exist_ok=True)

    report_path = os.path.join(reports_folder, filename)

    with open(report_path, "w", encoding="utf-8") as file:
        file.write(content)

    return report_path
