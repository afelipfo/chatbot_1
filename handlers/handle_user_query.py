# handlers/handle_user_query.py

import chainlit as cl
from handlers.router import router

# Main handler for user queries
async def handle_user_query(question: str, session_id: str = None):
    # ✅ Only try to get session_id from Chainlit if it's not provided (avoids ContextVar error)
    if session_id is None:
        try:
            session_id = cl.user_session.get("session_id", "default_session")
        except LookupError:
            session_id = "test_session"  # Fallback for non-Chainlit environments

    return await router(question, session_id)  # ✅ Pass both arguments




