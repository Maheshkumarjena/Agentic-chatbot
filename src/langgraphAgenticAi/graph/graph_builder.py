from langgraph.graph import END, START, StateGraph

from src.langgraphAgenticAi.state.state import State
from src.langgraphAgenticAi.nodes.basic_chatbot_node import BasicChatbotNode

class GraphBuilder:
    def __init__(self, model):
        self.llm = model
        self.graph_builder = StateGraph(State)

    def basic_chatbot_build_graph(self):
        """
        Builds a basic chatbot graph using LangGraph.
        """

        basic_chatbot_node = BasicChatbotNode(self.llm)
        self.graph_builder.add_node("chatbot", basic_chatbot_node.process)
        self.graph_builder.add_edge(START, "chatbot")
        self.graph_builder.add_edge("chatbot", END)
        return self.graph_builder.compile()

    def setup_graph(self, usecase):
        """
        Sets up the graph for the selected use case.
        """
        if usecase == "Basic Chatbot":
            return self.basic_chatbot_build_graph()

        raise ValueError(f"Unsupported use case: {usecase}")