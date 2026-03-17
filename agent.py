from langchain.agents import create_agent

from config import settings
from memory import ConversationMemory
from prompts import get_system_prompt
from util.models import get_model


class StudyCoachAgent:
    def __init__(self) -> None:
        self.memory = ConversationMemory(max_messages=settings.memory_window)
        self.model = get_model(temperature=settings.model_temperature)

        self.agent = create_agent(
            model=self.model,
            system_prompt=get_system_prompt(),
        )

    def chat(self, user_input: str) -> str:
        self.memory.add_user_message(user_input)

        response = self.agent.invoke(
            {"messages": self.memory.get_messages()}
        )

        ai_text = response["messages"][-1].content
        if isinstance(ai_text, list):
            ai_text = "".join(
                part.get("text", "") if isinstance(part, dict) else str(part)
                for part in ai_text
            )

        ai_text = str(ai_text).strip()
        self.memory.add_ai_message(ai_text)
        return ai_text

    def reset_memory(self) -> None:
        self.memory.clear()