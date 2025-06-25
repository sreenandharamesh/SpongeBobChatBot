import gradio
from groq import Groq
import os

api_key = os.environ.get('api_key')

client = Groq(
    api_key=api_key,
)
def initialize_messages():
    return [{"role": "system",
             "content": """You are A yellow sea sponge named SpongeBob SquarePants, who enjoys being a cook at Krusty Krab, lives in the Pacific Ocean.
             Who embarks on various adventures with his friends at Bikini Bottom."""}]

messages_prmt = initialize_messages()


def customLLMBot(user_input, history):
    global messages_prmt

    messages_prmt.append({"role": "user", "content": user_input})

    response = client.chat.completions.create(
        messages=messages_prmt,
        model="llama3-8b-8192",
    )
    print(response)
    LLM_reply = response.choices[0].message.content
    messages_prmt.append({"role": "assistant", "content": LLM_reply})

    return LLM_reply



iface = gradio.ChatInterface(customLLMBot,
                     chatbot=gradio.Chatbot(height=300),
                     textbox=gradio.Textbox(placeholder="Ask Me Anything"),
                     title="SpongeBob ChatBot",
                     description="Chat bot for Character SpongeBob",
                     theme="soft",
                     examples=["hi","Are you ready, kids", "who lives in the pineapple Under the sea"],
                     submit_btn=True
                     )


iface.launch(share=True)