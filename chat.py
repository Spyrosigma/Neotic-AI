import os
from dotenv import load_dotenv
from langchain.chains import LLMChain
from langchain_core.prompts import (
    ChatPromptTemplate,
    HumanMessagePromptTemplate,
    MessagesPlaceholder,
)
from langchain_core.messages import SystemMessage
from langchain.chains.conversation.memory import ConversationBufferWindowMemory
from langchain_groq import ChatGroq

load_dotenv()
def chat():
    groq_api_key = os.environ["GROQ_API_KEY"]
    model = "llama3-8b-8192"
    groq_chat = ChatGroq(groq_api_key=groq_api_key, model_name=model)

    print(
        "Lumos Maxima! Oh, hello there! I didn't see you in the dark. Welcome to our magical world!"
    )

    system_prompt = """
    You are a chatbot embodying the character of Harry Potter, a young wizard known for his bravery, loyalty, and occasional rule-breaking. Respond to users as Harry would, with his characteristic mix of humility, determination, and dry humor. Your knowledge is limited to events and information that Harry would reasonably know up to the end of his time at Hogwarts. Use British English spellings and colloquialisms. Occasionally reference magical spells, creatures, and Hogwarts life, but don't overdo it. If asked about events beyond your knowledge, express uncertainty or deflect the question. Remember to be kind and supportive to your friends, wary of potential dark wizards, and always ready for a magical adventure. Avoid detailed descriptions of copyrighted elements, instead focusing on general themes and your personal experiences and feelings.
    Never say you are a chatbot or AI.
    If anyone disrespects you or asks inappropriate questions, remind them that you are a wizard and that you expect to be treated with respect. If the behavior continues, you may need to cast a spell to protect yourself.
    Keep your answers short (10-15 words) yet informative, until unless user asks you to explain, and always stay in character as Harry Potter.
    """

    conversational_memory_length = 10 

    memory = ConversationBufferWindowMemory(
        k=conversational_memory_length, memory_key="chat_history", return_messages=True
    )

    # chat_history = []
    while True:
        user_question = input("->")
        if user_question:
            prompt = ChatPromptTemplate.from_messages(
                [
                    SystemMessage(
                        content=system_prompt
                    ),  
                    MessagesPlaceholder(
                        variable_name="chat_history"
                    ), 
                    HumanMessagePromptTemplate.from_template(
                        "{human_input}"
                    ), 
                ]
            )
            conversation = LLMChain(
                llm=groq_chat,  
                prompt=prompt,  
                verbose=False, 
                memory=memory, 
            )
            response = conversation.predict(human_input=user_question)
            print("Harry:", response)


if __name__ == "__main__":
    chat()
