from openai import OpenAI
from rag import retrieve_context
from memory import add_memory
import tools


client = OpenAI()

SYSTEM_PROMPT = """
You are an AI assistant.

You have access to these tools:

• time → returns current time (HH:MM:SS)
• datetime → returns current date and time
• calculator → evaluates mathematical expressions (e.g., 12*5, 100/2)

If a tool is needed, respond EXACTLY in this format:

TOOL:tool_name:argument

Examples:
TOOL:time
TOOL:datetime
TOOL:calculator:12*5+8

If no tool is needed, answer normally in Turkish.
"""

def run_agent(user_input: str):

    # 1) RAG context al
    context = retrieve_context(user_input)

    prompt = f"""
Context:
{context}

User:
{user_input}
"""

    # 2) LLM çağrısı
    res = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": prompt}
        ]
    )

    msg = res.choices[0].message.content.strip()

    # 3) Tool kontrolü
    if msg.startswith("TOOL:"):

        parts = msg.split(":", 2)
        tool_name = parts[1].strip()
        arg = parts[2].strip() if len(parts) > 2 else None

        if tool_name in tools.TOOLS:
            try:
                if arg:
                    tool_result = tools.TOOLS[tool_name](arg)
                else:
                    tool_result = tools.TOOLS[tool_name]()

                final = f"Tool result: {tool_result}"

            except Exception as e:
                final = f"Tool error: {str(e)}"

        else:
            final = "Tool not found."

    else:
        final = msg

    # 4) Memory kaydı
    add_memory(f"User: {user_input} | Assistant: {final}")

    return final
