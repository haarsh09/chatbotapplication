import streamlit as st
from llama_index.core import SimpleDirectoryReader
from llama_index.core import ServiceContext
from llama_index.llms.openai import OpenAI
from llama_index.core import VectorStoreIndex
import os
from dotenv import load_dotenv
import openai
import time


load_dotenv()


openai.api_key = os.getenv("OPENAI_API_KEY")


with st.sidebar:
    st.title("Flight booking FAQs")
    st.markdown('''
    ## About
    Chat with your data using a chatbot powered by OpenAI's GPT-3.5.
    ''')


if 'conversation_history' not in st.session_state:
    st.session_state.conversation_history = []


FALLBACK_RESPONSE = "I'm sorry, I don't have an answer to that. Can you please rephrase or ask something else?"

def main():
    st.header("Chat with a customer care agent to resolve queries!!")
    knowledgebase_dir = 'knowledgebase'

    
    reader = SimpleDirectoryReader(input_dir='knowledgebase', recursive=True)
    docs = reader.load_data()

    
    service_context = ServiceContext.from_defaults(
        llm=OpenAI(model="gpt-3.5-turbo", temperature=0.5, system_prompt="You are a customer care agent for a flight booking agency, answer all the questions professionally and appropriately")
    )

    
    index = VectorStoreIndex.from_documents(docs, service_context=service_context)

    
    query = st.text_input("Ask your queries here...")

    if query:
        
        chat_engine = index.as_chat_engine(chat_mode="condense_question", verbose=True)
        response = chat_engine.chat(query)

        
        response_text = response.response

        
        st.session_state.conversation_history.append(f"User: {query}")
        st.session_state.conversation_history.append(f"Bot: {response_text}")

        
        st.write(response_text)

    
    if st.session_state.conversation_history:
        st.write("### Conversation History")
        for line in st.session_state.conversation_history:
            st.write(line)


if __name__ == '__main__':
    main()
