# Agentic ChatBot

This project provides a Streamlit UI for running a LangGraph-based agentic chatbot with either Groq or Ollama as the LLM backend.

## Setup

Install the dependencies first:

```bash
pip install -r requirements.txt
```

Then start the app:

```bash
streamlit run app.py
```

The UI reads its options from `src/langgraphAgenticAi/ui/uiConfigFile.ini`.

## Groq

Groq is the hosted option. Use it when you want a cloud model without running anything locally.

How to use it:

1. Set `LLM` to `Groq` in the UI.
2. Enter your Groq API key in the UI, or set the `GROQ_API_KEY` environment variable before launching the app.
3. Choose one of the Groq models listed in the dropdown.
4. Enter your message and send it.

Example environment variable setup on Windows PowerShell:

```powershell
$env:GROQ_API_KEY = "your_groq_api_key"
streamlit run app.py
```

The Groq wrapper uses the selected model directly through `langchain_groq.ChatGroq`.

Available Groq models in the UI include:

- `meta-llama/llama-4-scout-17b-16e-instruct`
- `meta-llama/llama-prompt-guard-2-22m`
- `meta-llama/llama-prompt-guard-2-86m`
- `openai/gpt-oss-safeguard-20b`
- `qwen/qwen3-32b`
- `qwen/qwen3.6-27b`

## Ollama

Ollama is the local option. Use it when you want to run a model on your machine.

How to use it:

1. Install and start Ollama locally.
2. Pull at least one model, for example:

```bash
ollama pull llama3.1:8b
```

3. Set `LLM` to `Ollama` in the UI.
4. Pick one of the Ollama models from the dropdown.
5. Keep the Ollama server running at `http://localhost:11434`, or change the base URL in the UI if your Ollama server is hosted elsewhere.
6. Enter your message and send it.

The Ollama wrapper uses `langchain_community.chat_models.ChatOllama` with `temperature=0`.

Available Ollama models in the UI include:

- `llama3.1:8b`
- `mistral:7b`
- `qwen2.5:7b`
- `phi3:mini`

## Notes

- The app currently supports the `Basic Chatbot` use case.
- If no Groq key is provided, the app will look for `GROQ_API_KEY`.
- If no Ollama model is selected, the app will prompt you to choose one.
