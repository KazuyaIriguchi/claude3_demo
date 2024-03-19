from anthropic import Anthropic

client = Anthropic()

message = client.messages.create(
    max_tokens=1024,
    messages=[
        {
            "role": "user",
            "content": "Hello, Claude.",
        }
    ],
    model="claude-3-haiku-20240307",
)
print(message.content)

