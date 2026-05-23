import gradio as gr
from transformers import pipeline

# Open Source Model
chatbot = pipeline(
    "text-generation",
    model="Qwen/Qwen2.5-0.5B-Instruct"
)

# Memory
conversation_history = []

def chat(message, history):

    prompt = ""

    for user, bot in history:
        prompt += f"User: {user}\nAssistant: {bot}\n"

    prompt += f"User: {message}\nAssistant:"

    response = chatbot(
        prompt,
        max_new_tokens=100
    )

    answer = response[0]["generated_text"].split("Assistant:")[-1]

    history.append((message, answer))

    return history

demo = gr.ChatInterface(
    fn=chat,
    title="AI Personal Assistant"
)

demo.launch()
