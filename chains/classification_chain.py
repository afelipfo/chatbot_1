# chains/classification_chain.py

from langchain.schema.runnable import RunnableLambda
from config.settings import llm, classification_memory
from prompts.classification_prompt import classification_prompt

# Function for classification
async def classify(question):
    return await llm.ainvoke(classification_prompt.format(question=question))

classification_chain = RunnableLambda(classify)
