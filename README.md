
## 13. Python Implementation

This project includes a working Python prototype of an Agentic AI Research Assistant.

### Features
- Accepts research questions from users.
- Creates a research plan.
- Selects a knowledge retrieval tool.
- Searches a local research knowledge base.
- Analyzes retrieved information.
- Generates and saves research reports.

### Project Structure

```text
agentic-ai-research-assistant/
├── README.md
├── case-study.md
├── main.py
├── agent.py
├── tools.py
├── knowledge_base.json
├── requirements.txt
├── .gitignore
└── reports/
```

### Requirements
- Python 3.10 or later

### How to Run

Activate the virtual environment:

```powershell
.venv\Scripts\Activate.ps1
```

Run the application:

```powershell
python main.py
```

Enter a research question when prompted.

Type `exit` to close the application.

### Generated Reports

Research reports are saved in the `reports/` directory.

### Current Implementation

This is a local prototype using keyword-based retrieval and a predefined knowledge base. It does not yet connect to a live search engine or an external language model.
