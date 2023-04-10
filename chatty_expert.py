from llama_index import GPTSimpleVectorIndex, Document, SimpleDirectoryReader
import os
import pyaudio
import wave
from tqdm import tqdm
import sys
import json
import base64
import time
import speech_recognition as sr
from gtts import gTTS
import os
from playsound import playsound
from dotenv import load_dotenv
import requests

load_dotenv()
os.environ['OPENAI_API_KEY'] = os.getenv('OPENAI_API_KEY')
ELEVENLABS_API_KEY = os.getenv('ELEVENLABS_API_KEY')

documents = SimpleDirectoryReader('data').load_data()

if os.path.exists('index.json'):
    index = GPTSimpleVectorIndex.load_from_disk('index.json')
else:
    index = GPTSimpleVectorIndex(documents)
    index.save_to_disk('index.json')

### Voice input
def record_audio(wave_out_path, record_second,rounds):
    CHUNK = 1024
    FORMAT = pyaudio.paInt16
    CHANNELS = 1  # 2
    RATE = 16000  # 44100
    p = pyaudio.PyAudio()
    stream = p.open(format=FORMAT,
                    channels=CHANNELS,
                    rate=RATE,
                    input=True,
                    frames_per_buffer=CHUNK)
    wf = wave.open(wave_out_path, 'wb')
    wf.setnchannels(CHANNELS)
    wf.setsampwidth(p.get_sample_size(FORMAT))
    wf.setframerate(RATE)
    print(f"* What is your round {rounds} question? You have {record_second} seconds to complete your questions. If you want to stop, say 'stop chatting' \n")
    for i in tqdm(range(0, int(RATE / CHUNK * record_second))):
        data = stream.read(CHUNK)
        wf.writeframes(data)
    print("* The bot is processing\n")
    stream.stop_stream()
    stream.close()
    p.terminate()
    wf.close()

def audio2text(wave_out_path):
    r = sr.Recognizer()
    with sr.AudioFile(wave_out_path) as source:
        # listen for the data (load audio to memory)
        audio_data = r.record(source)
        # recognize (convert from speech to text)
        text = r.recognize_google(audio_data)
        print('Your question is:',text,'\n')
        return text
    
def text2speech(text, out_path, lang = 'en'):
    headers = {
        'accept': 'audio/mpeg',
        'xi-api-key': ELEVENLABS_API_KEY,
        'Content-Type': 'application/json',
    }

    json_data = {
        'text': text,
    }

    response = requests.post('https://api.elevenlabs.io/v1/text-to-speech/pNInz6obpgDQGcFmaJgB', headers=headers, json=json_data)

    with open(out_path, 'wb') as f:
        f.write(response.content)

    # play the speech using the default media player
    playsound(out_path)

    # remove file onece done
    if os.path.isfile(out_path):
        os.remove(out_path)



if __name__ == '__main__': 
    rounds = 1
    while True:  # Can record several times depending on your need. 
        record_audio("output/input.wav", record_second=5, rounds = rounds) #set recording time
        ### Voice-to-text
        text = audio2text("output/input.wav")

        if text.lower() == 'stop chatting':
            print(f'You have {rounds} rounds of conversations with the book, good job!')
            break

        else:
            ### Search response
            response = index.query(text)

            ### Response to speech
            print(response.response)
            print('--'*50)
            text2speech(response.response.replace('\n',''),  "output/output.mp3")

        rounds += 1



        