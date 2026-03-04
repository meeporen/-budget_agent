from langchain_openai import ChatOpenAI
from config import settings


llm = ChatOpenAI(
    base_url=settings.lm_studio_base_url,
    api_key="lm-studio",
    model=settings.model,
    temperature=settings.temperature,
)

__all__ = ["llm"]