### Define the API base URL and model name
VL_LLM_API_BASE = "http://192.168.100.27:9602/v1"
VL_MODEL_NAME= 'Qwen_vl'
VL_MAX_TOKENS=20000
TIME_OUT = 600

LLM_API_BASE = "http://192.168.100.27:15001/v1/"
MODEL_NAME = "qwen3-32b"


import asyncio
## for openai model, use functionAgent class
# from llama_index.llms.openai import OpenAI
# from llama_index.core.agent.workflow import FunctionAgent
## for non openai model, use workflow ReActAgent class
from llama_index.llms.openai_like import OpenAILike
from llama_index.core.agent.workflow import ReActAgent
from llama_index.tools.yahoo_finance import YahooFinanceToolSpec

llm = OpenAILike(
            model=MODEL_NAME,
            api_base=LLM_API_BASE,
            api_key='EMPTY',
            is_chat_model=True,
            temperature=0.7,
            # max_tokens=MAX_TOKENS,
            timeout=TIME_OUT,
            additional_kwargs={"extra_body": {"chat_template_kwargs": {"enable_thinking": False}}},
        )

# Define a simple calculator tool
def multiply(a: float, b: float) -> float:
    """Useful for multiplying two numbers."""
    return a * b

def add(a: float, b: float) -> float:
    """Add two numbers and returns the sum"""
    return a + b

finance_tools = YahooFinanceToolSpec().to_tool_list()
finance_tools.extend([multiply, add])

# Create an agent workflow with our calculator tool
agent = ReActAgent(
    tools=[multiply],
    llm=llm,
    system_prompt="You are a helpful assistant that can perform basic mathematical operations using tools",
)

# async def main():
#     # Run the agent
#     response = await agent.run("20+(2*4)?")
#     print(str(response))

workflow = ReActAgent(
    name="Agent",
    description="Useful for performing financial operations.",
    llm=llm,
    tools=finance_tools,
    system_prompt="You are a helpful assistant.",
)


async def main():
    response = await workflow.run(
        user_msg="What's the current stock price of AAPL?"
    )
    print(response)



# Run the agent
if __name__ == "__main__":
    asyncio.run(main())