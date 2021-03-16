import pyttsx3
import requests
import json

engine = pyttsx3.init()
voices = engine.getProperty('voices')

rate = engine.getProperty('rate')   # getting details of current speaking rate
print (rate)                        #printing current voice rate
engine.setProperty('rate', 150)     # setting up new voice rate
engine.setProperty('voice', voices[-1].id)

url = "https://official-joke-api.appspot.com/random_ten"

response = requests.get(url)
print(response.status_code)
json_data = json.loads(response.text)
# print(json_data)

class Joke:
    def __init__(self, setup, punchline)-> None:
        self.setup = setup
        self.punchline = punchline

    def __str__(self) -> str:
        return f"setup: {self.setup}, punchline: {punchline}"


jokes = []

for j in json_data:
    setup = j["setup"]
    punchline = j['punchline']
    joke = Joke(setup, punchline)
    jokes.append(joke)


for joke in jokes:
    print(joke)
    pyttsx3.speak("Setup")
    pyttsx3.speak(joke.setup)
    pyttsx3.speak("Punchline")
    pyttsx3.speak(joke.punchline)