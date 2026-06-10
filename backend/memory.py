chat_memory = {}


def save_message(user, role, content):

    if user not in chat_memory:
        chat_memory[user] = []

    chat_memory[user].append(
        {
            "role": role,
            "content": content
        }
    )


def get_memory(user):

    return chat_memory.get(user, [])
