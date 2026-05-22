import autogen

# Configure AutoGen to use Ollama's API endpoint
config_list = [
    {
        "model": "llama3.1:latest",  
        "api_base": "http://localhost:11434/v1",
        "api_key": "ollama",  
        "api_type": "ollama",
    }
]

# Create an LLM configuration
llm_config = {
    "config_list": config_list,
    "temperature": 0.7,
    "timeout": 120,  
}

# Create agents that use your local model
assistant = autogen.AssistantAgent(
    name="assistant",
    llm_config=llm_config
)

user_proxy = autogen.UserProxyAgent(
    name="user_proxy",
    human_input_mode="TERMINATE",
    code_execution_config={"work_dir": "coding", "use_docker": False}
)

# Start a conversation
user_proxy.initiate_chat(
    assistant,
    message="Explain what a recursive function is with a simple Python example."
)