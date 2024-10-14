#paste api key here

from groq import Groq

client = Groq(
    api_key="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",
)

chat_completion = client.chat.completions.create(
    messages=[
        {
            "role": "user",
            "content": "Explain the importance of fast language models",
        }
    ],
    model=" llama-3.2-3b-preview",
)

print(chat_completion.choices[0].message.content)
