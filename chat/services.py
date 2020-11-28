def serialize_messages(messages):
    """Вна2ре"""
    serialized_messages = []
    for message in messages:
        serialized_message = {
            'text': message.text,
            'time': message.time.strftime("%Y-%m-%d %H:%M:%S"),
            'user': message.user.username,
        }
        serialized_messages.append(serialized_message)
    return serialized_messages