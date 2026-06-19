import streamlit as st
import os

from src.langgraphAgenticAi.ui.uiConfigFile import Config

class LoadStreamlitUI:
    def __init__(self):
        self.config = Config()
        self.user_controls = {}

    def load_streamlit_ui(self):
        st.set_page_config(page_title=self.config.get_page_title())
        st.title(self.config.get_page_title())

        with st.sidebar:
            # Get options from the config file
            llm_options = self.config.get_llm_options()
            usecase_options = self.config.get_usecase_options()

            # LLM selection
            self.user_controls['llm'] = st.selectbox("Select LLM", llm_options)

            # Model Selection (Groq)
            if self.user_controls.get('llm') == 'Groq':
                model_options = self.config.get_groq_model_options()
                self.user_controls['groq_model'] = st.selectbox("Select Groq Model", model_options)
                # Ensure a default exists in session_state before creating the widget
                if 'groq_api_key' not in st.session_state:
                    st.session_state['groq_api_key'] = ''

                self.user_controls['groq_api_key'] = st.text_input("API Key", type="password", key="groq_api_key")

                if not self.user_controls['groq_api_key']:
                    st.warning("Please enter your Groq API key to proceed. You can obtain it from https://console.groq.ai/")

            # Use case selection
            self.user_controls['selected_usecase'] = st.selectbox("Select Use Case", usecase_options)

        return self.user_controls