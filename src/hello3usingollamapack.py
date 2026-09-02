
import sys
import ollama

#Initiate the ollama clinet
client = ollama.Client()


def ask(question: str) -> str:
    """Send one question to the LLM and return the answer text."""
    resp = client.chat(
        model="llama3.1",
        messages=[
            {"role": "system", "content": "You are concise. Assume AI/ML context when the question is ambiguous." },
            {"role": "user",   "content": question},
        ],
        options={"temperature": 0.3},
    )
    return resp["message"]["content"]


if __name__ == "__main__":
    q = " ".join(sys.argv[1:]) or "Say hello in one sentence."
    print(ask(q))

'''
if __name__ == "__main__":
    q = " ".join(sys.argv[1:]) or "Say hello in one sentence."
    print(query_local_llm('smollm:1.7b',q))

'''