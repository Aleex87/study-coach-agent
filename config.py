from dataclasses import dataclass


@dataclass(frozen=True)
class Settings:
    agent_name: str = "Study Coach Agent"
    model_temperature: float = 0.2
    memory_window: int = 10


settings = Settings()