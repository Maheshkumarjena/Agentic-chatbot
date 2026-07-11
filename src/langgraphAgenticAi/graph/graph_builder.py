from langgraph.graph import StateGraph 
from src.langgraphAgenticAi.state.state import State
from langgraph.graph import START,END 

class GraphBuilder : 
    def __init__(self,model):
        self.llm = model 
        self.graph_builder = StateGraph(State)

    def basic_chatbot_build_graph(self):
        """
        Builds a basic chatbot graph using LangGraph.This method initializes a chatbot node using the `BasicChatbotNode` class and adds it to the graph.The chatbot node is set as both the entry and exit point of the graph, allowing for a simple conversational flow. The method returns the constructed graph for further use or execution.
        """

        self.graph_builder.add_node("chatbot","")
        self.graph_builder.add_edge(START,"chatbot")
        self.graph_builder.add_edge("chatbot",END)
        self.basic_chatbot_node = BasicChatbotNode(self.llm)