import queue
import sys
import sounddevice as sd
import json
from vosk import Model, KaldiRecognizer
class Recognizer:
    def __init__(self):
        self.q = queue.Queue()
        self.device = None
        self.device_info = sd.query_devices(self.device, "input")
        self.samplerate = self.device_info["default_samplerate"]
        self.model = Model(lang="en-us")
        self.recognizer = KaldiRecognizer(self.model, self.samplerate)

    def callback(self, indata, frames, time, status):
        """This is called (from a separate thread) for each audio block."""
        if status:
            print(status, file=sys.stderr)
        self.q.put(bytes(indata))

    def wait_command(self):
        try:
            with sd.RawInputStream(samplerate=self.samplerate, blocksize=8000, device=self.device,
                                   dtype="int16", channels=1, callback=self.callback):
                while True:
                    data = self.q.get()
                    if self.recognizer.AcceptWaveform(data):
                        cur = json.loads(self.recognizer.Result())
                        if cur["text"] != "":
                            return cur["text"]

        except KeyboardInterrupt:
            return "exit command"
