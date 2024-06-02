import shutil
import asyncio
import argparse

import ollama

messages = [{'role': 'system', 'content': 'A dialog, where User interacts with his friend. Friend smart, funny and answer briefly. You need only answer for last message of User.'},{'role': 'user', 'content': 'Why is the sky blue?'}]
response = ollama.chat(
    model="gemma:2b",
    messages=messages
)

print(response['message']['content'])