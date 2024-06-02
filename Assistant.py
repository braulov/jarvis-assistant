from Recognizer import Recognizer
from Chat import Chat
from TextToSpeech import TextToSpeech
class Assistant:
    def __init__(self):
        self.recognizer = Recognizer()

        self.chat = Chat()
        self.context = [{'role':'system', 'content': self.chat.system_prompt}]
        self.voice_generator = TextToSpeech()
        self.size_of_dialog = 0
    def update_context(self):
        self.context = (self.context[-500:]) if len(self.context) >= 500 else self.context
    def createDialog(self):
        while True:
            command = self.recognizer.wait_command()
            if command == "exit command":
                print("Friend: Bye bye!")
                exit()
            self.update_context()
            print(f"You: {command}")
            self.context.append({'role':'user','content':(command+'\n')})
            answer = self.chat.answer(self.context)
            print('Friend: ', answer)
            self.voice_generator.generate(answer)
            self.context.append({'role':'assistant','content':(answer+'\n')})
