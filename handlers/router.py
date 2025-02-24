# handlers/router.py

import chainlit as cl
from chains.classification_chain import classification_chain
from chains.conversation_chain import conversation_chain
from functions.rag_chain import rag_chain
from functions.web_search_chain import web_search_chain
from functions.policy_optimizer_chain import policy_optimizer_chain

# Router function to direct the question to the appropriate chain
async def router(question: str, session_id: str):
    try:
        # ✅ Ensure session_id is set
        if not session_id:
            session_id = cl.user_session.get("session_id", "default_session")

        # Example: Check if classification_chain supports async execution
        if hasattr(classification_chain, "ainvoke"):  
            return await classification_chain.ainvoke({"input": question, "session_id": session_id})
        else:
            return await asyncio.to_thread(classification_chain.invoke, {"input": question, "session_id": session_id})

    except Exception as e:
        return f"Ocurrió un error en router: {str(e)}"
