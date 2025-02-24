#main.py

import chainlit as cl
import asyncio
from uuid import uuid4
from handlers.handle_user_query import handle_user_query

# Chainlit events to handle the chat
@cl.on_chat_start
async def on_chat_start():
    session_id = str(uuid4())  # Generate session ID
    cl.user_session.set("session_id", session_id)  # Store session ID
    await cl.Message(content="¡Bienvenido! ¿Cómo puedo ayudarte con tus consultas sobre seguros hoy?").send()

@cl.on_message
async def on_message(message: cl.Message):
    msg = cl.Message(content="Procesando tu solicitud...")
    await msg.send()

    try:
        session_id = cl.user_session.get("session_id", "default_session")  # Retrieve session ID
        response = await handle_user_query(message.content, session_id)  # Pass both arguments

        msg.content = response
        await msg.update()
    except Exception as e:
        msg.content = f"Ocurrió un error: {str(e)}"
        await msg.update()

@cl.on_chat_end
async def on_chat_end():
    await cl.Message(content="¡Gracias por usar nuestro servicio de asistencia en seguros! Si tienes más preguntas en el futuro, no dudes en volver.").send()

# ✅ Corrected async execution
if __name__ == "__main__":
    async def run_test():
        test_query = "How do I optimize my insurance policy?"
        test_session_id = "test_session"
        response = await handle_user_query(test_query, test_session_id)
        print(response)

    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    loop.run_until_complete(run_test())
    loop.close()

