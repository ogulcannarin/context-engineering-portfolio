from memory import search_memory

def retrieve_context(query: str):
    memories = search_memory(query)
    return "\n".join(memories) if memories else ""
