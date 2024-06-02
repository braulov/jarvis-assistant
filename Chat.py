import ollama

class Chat:
    def __init__(self):
        self.system_prompt = 'A dialog, where User interacts with his friend. Friend smart, funny and answer briefly. You need only answer for last message of User.'
        self.model = 'gemma:2b'
    def answer(self,context):
        result = ollama.chat(model=self.model,messages=context)
        return result['message']['content']