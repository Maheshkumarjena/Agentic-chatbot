import os 
import streamlit as st
from langchain_groq import Chatgroq

class GroqLlm:
    def __init__(self , api_key: str):
        self.user_controls_input = user_controls_input

    def get_llm_model(self):
        try:
            groq_api_key = self.user_controls_input.get('groq_api_key')
            selected_groq_model = self.user_controls_input["groq_model"]

            if groq_api_key == '' and os.environ.get('GROQ_API_KEY') is None:
                st.error("Please enter your Groq API key to proceed. You can obtain it from https://console.groq.ai/")
                return None

                llm = Chatgroq(
                    api_key=groq_api_key,
                    model = selected_groq_model
                )

        except Exception as e:
            raise ValueError(f"Error initializing Groq LLM: {e}")
        return llm