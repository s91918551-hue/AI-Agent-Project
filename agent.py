from ollama import chat

print("AI Agent started!")
print("Type 'exit' to stop.")

while True:
    question = input("You: ")

    if question.lower() == "exit":
        break

    response = chat(
        model="llama3.2",
        messages=[
            {"role": "user", "content": question}
        ]
    )

    print("AI:", response.message.content)