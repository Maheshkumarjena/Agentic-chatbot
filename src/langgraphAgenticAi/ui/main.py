import streamlit as st
from src.langgraphAgenticAi.ui.streamlitui.loadui import LoadStreamlitUI
from src.langgraphAgenticAi.ui.streamlitui.display_result import DisplayResultStreamlit
from src.langgraphAgenticAi.graph.graph_builder import GraphBuilder
from src.langgraphAgenticAi.llms.groqllm import GroqLlm
from src.langgraphAgenticAi.llms.ollama_llm import OllamaLlm

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
        try:
            selected_llm = user_controls.get('llm')

            if selected_llm == 'Groq':
                model = GroqLlm(user_controls).get_llm_model()
            elif selected_llm == 'Ollama':
                model = OllamaLlm(user_controls).get_llm_model()
            else:
                st.warning("Please select a supported LLM.")
                return

            if model is None:
                return

            usecase = user_controls.get('selected_usecase')
            if not usecase:
                st.warning("Please select a valid use case from the dropdown.")
                return        
            graph_builder = GraphBuilder(model=model)
            try:
                graph = graph_builder.setup_graph(usecase=usecase)
                DisplayResultStreamlit(usecase, graph, user_message).display_result_on_ui() 
            except Exception as e:
                st.error(f"An error occurred while setting up the graph: {str(e)}")
                return

        
        except Exception as e:
            st.error(f"An error occurred while processing the user input: {str(e)}")