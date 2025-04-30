from google.adk.agents import Agent
from google.adk.models.lite_llm import LiteLlm
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv(dotenv_path=os.path.join(os.path.dirname(__file__), '..', '..', '.env'))

# Newscaster Summarizer Agent

def create_summarizer_agent():
    # Define a LiteLlm instance for summarization
    llm = LiteLlm(model="gemini/gemini-1.5-pro-latest", api_key=os.environ.get("GOOGLE_API_KEY"))

    summarizer = Agent(
        name="newscaster_summarizer_agent",
        description="Summarizes a list of Reddit post titles in a newscaster style.",
        model=llm,
        instruction=(
            "You are a news anchor summarizing Reddit headlines. "
            "Given a list of post titles, provide a concise, engaging summary in a professional newscaster style. "
            "Highlight key themes or interesting points found only in the titles. "
            "Start with a captivating catchphrase or intro. Keep it brief."
            "If asked by the user, filter out unrelevant posts/subjects."
        )
    )
    return summarizer

# Expose root_agent for ADK
root_agent = create_summarizer_agent()