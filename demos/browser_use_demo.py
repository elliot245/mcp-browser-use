from langchain_openai import ChatOpenAI
from browser_use import Agent
from mcp_browser_use.utils import utils
import asyncio
from dotenv import load_dotenv
load_dotenv()

async def main():
    # Prepare LLM
    llm = utils.get_llm_model(
        provider="openai", model_name="gpt-4o", temperature=0.2
    )

    agent = Agent(
        task="Compare the price of gpt-4o and DeepSeek-V3",
        llm=llm,
        use_vision=False
    )
    await agent.run()

asyncio.run(main())
