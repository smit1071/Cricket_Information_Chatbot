# 🏏 Cricket Information Chatbot

A simple **Streamlit-based chatbot** built using **LangChain** and **Groq gemma2-9b-it**.  
This chatbot is designed exclusively to provide **cricket-related information** such as:

- ✅ Player statistics  
- ✅ Match schedules  
- ✅ Team information  
- ✅ Records  
- ✅ Rules of the game  

It remembers the conversation (using memory) and responds **conversationally**, while refusing unrelated queries.

---

## 🗂️ Project Structure
```
cricket_chatbot/
├─ __init__.py              # Marks this folder as a Python package
├─ app.py                   # Streamlit UI entry point
├─ config.py                # LLM configuration (GROQ API, model settings)
├─ chatbot/
│  ├─ __init__.py           # Marks chatbot module as a package
│  ├─ conversation.py       # Chatbot logic (LLM + Memory + Router)
│  └─ prompts.py            # System & few-shot prompt (cricket focus)
├─ requirements.txt         # Dependencies
└─ README.md                # Project documentation
```

---

## 🚀 How to Run

1. **Clone this repo**  
```bash
git clone https://github.com/your-username/cricket-chatbot.git
cd cricket_chatbot
```

2. **Create virtual environment**  
```bash
python -m venv venv
source venv/bin/activate     # Mac/Linux
venv\Scripts\activate      # Windows
```

3. **Install dependencies**  
```bash
pip install -r requirements.txt
```

4. **Set Groq API key**  
Export your API key as environment variable:

```bash
export GROQ_API_KEY="your_api_key_here"      # Mac/Linux
# OR in .env file (Windows)
GROQ_API_KEY="your_api_key_here"
```

5. **Run the app**  
```bash
streamlit run app.py
```

---

##  Features

- Built with **LangChain + Groq (gemma2-9b-it model)**
- Uses **ConversationBufferMemory** to maintain context
- Few-shot prompting to ensure cricket-only answers
- Refuses unrelated queries politely
- Simple, clean **Streamlit UI**

---

##  Example Usage

**User:** Who is Virat Kohli?  
**Bot:** Virat Kohli is an Indian cricketer, one of the best batsmen in the world. He has captained India and is known for his consistency, especially in ODI chases.  

**User:** Give me his ODI stats.  
**Bot:** He has scored over 13,000 ODI runs with an average above 57, including 47+ centuries.  

**User:** Tell me about football.  
**Bot:** Sorry, I can only provide cricket-related information.  

---

##  Tech Stack

- **LangChain** – LLM orchestration  
- **Groq gemma2-9b-it** – Open-source LLM backend  
- **Streamlit** – Simple frontend UI  

---

##  Limitation  

- As the chatbot relies on an LLM’s pretrained knowledge and conversation memory, its responses are limited to the LLM’s training data and may not always be up-to-date with live cricket data.

---

##  Possible Improvements  

- Integrate real-time **Cricket APIs** (e.g., player stats, live matches, schedules).  
 

