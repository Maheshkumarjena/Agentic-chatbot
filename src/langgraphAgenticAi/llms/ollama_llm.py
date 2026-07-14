import streamlit as st
from langchain_community.chat_models import ChatOllama


class OllamaLlm:
    def __init__(self, user_controls_input):
        self.user_controls_input = user_controls_input

    def get_llm_model(self):
        try:
            selected_ollama_model = self.user_controls_input.get("ollama_model")
            base_url = self.user_controls_input.get("ollama_base_url") or "http://localhost:11434"

            if not selected_ollama_model:
                st.error("Please select an Ollama model.")
                return None

            return ChatOllama(
                model=selected_ollama_model,
                base_url=base_url,
                temperature=0,
            )

        except Exception as error:
            raise ValueError(f"Error initializing Ollama LLM: {error}")