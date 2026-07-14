from configparser import ConfigParser

class Config: 
    def __init__(self, config_file='./src/langgraphAgenticAi/ui/uiConfigFile.ini'):
        self.config = ConfigParser()
        self.config.read(config_file)

    def _split_and_strip(self, value):
        return [item.strip() for item in value.split(',') if item.strip()]

    def get_llm_options(self):
        return self._split_and_strip(self.config['Default'].get("LLM_OPTIONS"))
          
    def get_usecase_options(self):
        return self._split_and_strip(self.config['Default'].get("USECASE_OPTIONS"))

    def get_groq_model_options(self):
        return self._split_and_strip(self.config['Default'].get("GROQ_MODEL_OPTIONS"))

    def get_ollama_model_options(self):
        return self._split_and_strip(self.config['Default'].get("OLLAMA_MODEL_OPTIONS"))
    
    def get_page_title(self):
        return self.config['Default'].get("PAGE_TITLE")
        

    def get(self, section, option):
        return self.config.get(section, option)

