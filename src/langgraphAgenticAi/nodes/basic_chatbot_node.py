from src.langgraphAgenticAi.state.state import State


class BasicChatbotNode:
    """
    A basic chatbot node that processes user input and generates responses.
    """

    def __init__(self, model):
        self.llm = model 

    
    def process(self , state:State)-> Dict:
        """
        Processes the input state and generates a response using the LLM model.
        Args:
            state (State): The current state containing user input and other relevant information.

    