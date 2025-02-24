# chains/conversation_chain.py

from langchain_core.runnables.history import RunnableWithMessageHistory
from config.settings import llm, shared_memory
from prompts.conversation_prompt import conversation_prompt

# Function to retrieve session history
def get_session_history(session_id: str):
    return shared_memory

# Define the conversation chain using the updated method
conversation_chain = RunnableWithMessageHistory(
    runnable=llm,
    get_session_history=get_session_history,
    input_messages_key="input",
    output_messages_key="output"
)
