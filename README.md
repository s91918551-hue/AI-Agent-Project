AI Agent Project

1. Project Overview

This project is a basic AI Agent developed using Python and the OpenAI API.

The AI Agent accepts a question or message from the user, sends it to the OpenAI API, and displays the AI-generated response in the terminal.

2. Objective

The main objective of this project is to understand how an AI Agent can:

- Accept input from a user
- Communicate with an AI model through an API
- Process the response
- Display the response to the user
- Use environment variables to protect API credentials

3. Technologies Used

- Python — Programming language
- OpenAI API — AI model communication
- python-dotenv — Loading environment variables
- Git & GitHub — Version control and project hosting
- VS Code — Development environment

4. How the AI Agent Works

User
  ↓
Enter a question
  ↓
Python AI Agent
  ↓
OpenAI API
  ↓
AI Model
  ↓
Generated Response
  ↓
User

5. Project Structure

AI-Agent-Project/
│
├── .gitignore
├── README.md
├── requirements.txt
├── ADR-001-Tech-Stack.md
├── agent.py
│
├── .env              # Private API key - not uploaded to GitHub
└── venv/             # Python virtual environment

6. Installation

Step 1: Create and activate the virtual environment

python -m venv venv

Activate it on Windows:

venv\Scripts\activate

Step 2: Install dependencies

pip install -r requirements.txt

If required, install the packages with:

pip install openai python-dotenv

7. API Key Configuration

Create a ".env" file in the project folder:

OPENAI_API_KEY=your_api_key_here

The ".env" file is included in ".gitignore" so that the API key is not uploaded to GitHub.

Never share your API key publicly.

8. Running the AI Agent

Run the following command from the project folder:

python agent.py

The program will display:

You:

Enter a question and press Enter.

9. Example

You: What is Artificial Intelligence?

AI Agent: Artificial Intelligence is a field of computer science...

10. Key Learning Outcomes

Through this project, I learned:

- Basic AI Agent architecture
- Using APIs in Python
- Environment variable management
- Python virtual environments
- Git and GitHub
- Creating an Architecture Decision Record (ADR)
- Building and testing a simple AI application

11. Future Improvements

The AI Agent can be extended in the future with:

- Conversation memory
- Web search
- File/document analysis
- Voice input and output
- A graphical user interface
- Multiple AI tools
- Task automation

12. Author

Student Project — AI-Augmented Workflow Course