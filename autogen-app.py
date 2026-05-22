import asyncio
from autogen_agentchat.conditions import TextMentionTermination
from autogen_agentchat.agents import UserProxyAgent, AssistantAgent
from autogen_agentchat.conditions import MaxMessageTermination
from autogen_agentchat.messages import TextMessage
#from autogen_ext.models.openai import OpenAIChatCompletionClient
from autogen_ext.models.ollama import OllamaChatCompletionClient
from autogen_agentchat.teams import RoundRobinGroupChat  
from autogen_agentchat.ui import Console


async def simple_user_agent():
    # Model client
    model_client = OllamaChatCompletionClient(model="llama3.1:latest")

    # Writer agent
    writer = AssistantAgent(
        "Writer",
        model_client=model_client,
        system_message=(
            "You are a professional writer. "
            "Always respond with a detailed draft when asked. "
        ),
    )

    # Reviewer agent
    reviewer = AssistantAgent(
        "Reviewer",
        model_client=model_client,
        system_message=(
            "You are a reviewer who critiques drafts and suggests improvements. "
        ),
    )

    # User proxy agent
    user_proxy = UserProxyAgent("User")

    # Termination conditions
    termination = MaxMessageTermination(max_messages=8)
    text_termination = TextMentionTermination("TERMINATE")

    # Group chat with Writer, Reviewer, and User
    team = RoundRobinGroupChat(
        [writer, reviewer, user_proxy],
        termination_condition=termination | text_termination,
        max_turns=8,
    )

    # Run the group chat
    await Console(
        team.run_stream(
            task=TextMessage(
                source=user_proxy.name,
                content="Please draft a comparison of CrewAI, LangGraph, and AutoGen."
            ),
        )
    )

if __name__ == "__main__":
    asyncio.run(simple_user_agent())