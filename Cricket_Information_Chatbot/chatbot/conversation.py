from langchain.chains import ConversationChain
from langchain.memory import ConversationBufferMemory
from langchain.prompts import PromptTemplate
from .prompts import SYSTEM_PROMPT
from config import load_llm

def get_chatbot():
    llm = load_llm()
    memory = ConversationBufferMemory()

    # Defining the conversation template with few-shot prompt
    template = SYSTEM_PROMPT + "\n\nConversation so far:\n{history}\nUser: {input}\nAssistant:"
    prompt = PromptTemplate(input_variables=["history", "input"], template=template)

    # Creating the chain with the LLM, memory, and prompt
    # The conversation chain will use the LLM to generate responses based on the chat history and user input
    conversation = ConversationChain(
        llm=llm,
        memory=memory,
        verbose=True
    )
    # Override the default prompt
    conversation.prompt = prompt  

    return conversation

