import streamlit as st
import os

from src.langgraphAgenticAi.ui.streamlitui.loadui import LoadStreamlitUI

def load_langgraph_agentic_app():
    """
    Load the LangGraph Agentic AI application using Streamlit Ui.
    This function initializes the Streamlit UI, sets the page title, and loads user controls based on the configuration file.
    Returns:
        dict: A dictionary containing user controls and selections from the Streamlit UI.

    
    """
     
    ui_loader = LoadStreamlitUI()
    user_controls = ui_loader.load_streamlit_ui()

    if not user_controls:
        st.warning("failed to load user input from the Streamlit UI. Please check the configuration file and ensure that all required options are provided.")
        return 
         

    user_message = st.chat_input("Enter your message:", key="user_message")

    if user_message:
        # configure llms
        obj_llm_config = {
            "llm": user_controls.get('llm'),
            "groq_model": user_controls.get('groq_model'),
            "groq_api_key": user_controls.get('groq_api_key'),
        }

        model = obj_llm_config.get('llm')

        if not model:
            st.warning("Please select a valid LLM from the dropdown.")
            return

        usecase = user_controls.get('selected_usecase')
        if not usecase:
            st.warning("Please select a valid use case from the dropdown.")
            return        