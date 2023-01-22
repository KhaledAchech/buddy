import speech_recognition as sr
import gtts
import requests
import json
import os

def run():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source)
        print("Say something!")
        audio = recognizer.listen(source)

    command = recognizer.recognize_google(audio)
    print("You said: " + command)

    api_key = "YOUR_API_KEY"
    prompt = command
    headers = {"Content-Type": "application/json", "Authorization": f"Bearer {api_key}"}
    data = """
    {
        """
    data += f'"prompt": "{prompt}",'
    data += """
        "model": "text-davinci-002",
        "temperature": 0.5,
        "max_tokens":100
    }
    """

    resp = requests.post("https://api.openai.com/v1/engines/davinci/completions",
                         headers=headers, data=data)

    result = json.loads(resp.text)
    response = result['choices'][0]['text']

    print(response)
    tts = gtts.gTTS(text=response, lang='en')
    tts.save("response.mp3")
    os.system("start response.mp3")
