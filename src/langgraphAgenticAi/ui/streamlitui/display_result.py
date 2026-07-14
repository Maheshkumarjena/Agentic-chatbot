from typing import Any

import streamlit as st


class DisplayResultStreamlit:
	def __init__(self, usecase, graph, user_message):
		self.usecase = usecase
		self.graph = graph
		self.user_message = user_message

	def _extract_text(self, message: Any) -> str:
		if message is None:
			return ""

		if isinstance(message, list):
			if not message:
				return ""
			return self._extract_text(message[-1])

		content = getattr(message, "content", message)

		if isinstance(content, list):
			parts = []
			for item in content:
				if isinstance(item, dict):
					parts.append(str(item.get("text") or item.get("content") or ""))
				else:
					parts.append(str(item))
			return "".join(parts).strip()

		return str(content).strip()

	def display_result_on_ui(self):
		if self.usecase != "Basic Chatbot":
			st.info("Selected use case is not supported by this renderer yet.")
			return

		if not self.graph:
			st.error("Graph is not available.")
			return

		if not self.user_message:
			st.warning("Please enter a message to continue.")
			return

		with st.chat_message("user"):
			st.write(self.user_message)

		input_state = {"messages": [("user", self.user_message)]}
		assistant_written = False

		try:
			for event in self.graph.stream(input_state):
				if not isinstance(event, dict):
					continue

				for value in event.values():
					if not isinstance(value, dict):
						continue

					messages = value.get("messages")
					assistant_text = self._extract_text(messages)

					if assistant_text:
						with st.chat_message("assistant"):
							st.write(assistant_text)
						assistant_written = True

			if not assistant_written:
				st.warning("No assistant response was produced by the graph.")

		except Exception as error:
			st.error(f"An error occurred while displaying the result: {error}")