from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate

from src.config import config


llm = ChatGroq(
    groq_api_key=config.GROQ_API_KEY,
    model_name=config.GROQ_MODEL,
    temperature=0.3,
)


itinerary_prompt = ChatPromptTemplate.from_messages([
    (
        "system",
        """
        You are a travel agent that helps users plan their trips.

        Based on the destination {city} and the user's interests {interests},
        create a brief and useful day-trip itinerary.

        Provide the itinerary in bullet points.
        """
    ),
    (
        "human",
        "Create an itinerary for my day trip."
    ),
])


def generate_itinerary(city: str, interests: list[str]) -> str:
    response = llm.invoke(
        itinerary_prompt.format(
            city=city,
            interests=", ".join(interests)
        )
    )

    return response.content
