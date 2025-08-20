# 🏏 Cricket Information Chatbot

A simple **Streamlit-based chatbot** built using **LangChain** and **Groq LLaMA3**.  
This chatbot is designed exclusively to provide **cricket-related information** such as:

- ✅ Player statistics  
- ✅ Match schedules  
- ✅ Team information  
- ✅ Records  
- ✅ Rules of the game  

It remembers the conversation (using memory) and responds **conversationally**, while refusing unrelated queries.

---

## 📂 Project Structure

cricket_chatbot/
│── app.py # Streamlit UI entry point
│── config.py # LLM configuration (Groq API key, model settings)
│── chatbot/
│ │── init.py
│ │── conversation.py # Chatbot logic (LLM + Memory + Prompt)
│ │── prompts.py # System + Few-shot prompt for cricket focus
│── requirements.txt # Dependencies
│── README.md # Project documentation




---

## 🚀 How to Run

1. **Clone this repo**  
```bash
git clone https://github.com/your-username/cricket-chatbot.git
cd cricket_chatbot



python -m venv venv
source venv/bin/activate     # Mac/Linux
venv\Scripts\activate        # Windows



Create virtual environment (optional but recommended)

python -m venv venv
source venv/bin/activate     # Mac/Linux
venv\Scripts\activate        # Windows


Install dependencies

pip install -r requirements.txt


Set Groq API key
Export your API key as environment variable:

export GROQ_API_KEY="your_api_key_here"      # Mac/Linux
setx GROQ_API_KEY "your_api_key_here"        # Windows (cmd)


Run the app

streamlit run app.py

🎯 Features

Built with LangChain + Groq (LLaMA3 model)

Uses ConversationBufferMemory to maintain context

Few-shot prompting to ensure cricket-only answers

Refuses unrelated queries politely

Simple, clean Streamlit UI

💡 Example Usage

User: Who is Virat Kohli?
Bot: Virat Kohli is an Indian cricketer, one of the best batsmen in the world. He has captained India and is known for his consistency, especially in ODI chases.

User: Give me his ODI stats.
Bot: He has scored over 13,000 ODI runs with an average above 57, including 47+ centuries.

User: Tell me about football.
Bot: Sorry, I can only provide cricket-related information.

📌 Tech Stack

LangChain – LLM orchestration

Groq LLaMA3 – Open-source LLM backend

Streamlit – Simple frontend UI