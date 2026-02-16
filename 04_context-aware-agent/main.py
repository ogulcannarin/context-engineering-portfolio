from agent import run_agent

print("Agent hazır! Çıkmak için 'exit' yaz.\n")

while True:
    user_input = input("You: ")

    if user_input.lower() == "exit":
        break

    response = run_agent(user_input)
    print("Agent:", response)
