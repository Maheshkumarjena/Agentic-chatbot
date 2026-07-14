from typing import Dict

from langchain_core.messages import AIMessage

from src.langgraphAgenticAi.state.state import State


class BasicChatbotNode:
    """
    A basic chatbot node that processes user input and generates responses.
    """

    def __init__(self, model):
        self.llm = model

    def process(self, state: State) -> Dict:
        """
        Process the input state and generate a response using the language model.
        """
        response = self.llm.invoke(state["messages"])

        if isinstance(response, str):
            response = AIMessage(content=response)

        return {"messages": [response]}