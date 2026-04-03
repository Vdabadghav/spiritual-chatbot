import chainlit as cl
from client import bot_response


@cl.on_chat_start
async def start():
    await cl.Message(
        content="Welcome to Spiritual AI\n\nAsk anything from Bhagavad Gita or Srimad Bhagavatam."
    ).send()


@cl.on_message
async def main(message: cl.Message):
    user_query = message.content

    msg = cl.Message(content="Thinking..")
    await msg.send()

    try:
        response = await bot_response(user_query)

        answer = response.get("answer", "No response found")

        msg.content = answer
        await msg.update()

    except Exception as e:
        msg.content = f" Error: {str(e)}"
        await msg.update()