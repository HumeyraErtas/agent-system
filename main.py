from agent import AgentSystem

agent = AgentSystem()

print("Agent sistemi hazır (çıkmak için 'exit')\n")

while True:
    q = input("Soru: ")

    if q.lower() == "exit":
        break

    print("\nCevap:\n", agent.handle_query(q), "\n")