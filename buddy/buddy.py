import speech_recognition as sr
import gtts
import openai
import os

def run():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source)
        print("Say something!")
        audio = recognizer.listen(source)

    command = recognizer.recognize_google(audio)
    print("You said: " + command)
    
    openai.api_key = "YOUR_API_KEY"
    prompt = command
    model = "text-davinci-002"
    max_tokens = 100

    # Send the POST request
    response = openai.Completion.create(
        engine=model,
        prompt=prompt,
        max_tokens=max_tokens,
        n=1,
        stop=None,
        temperature=0.5,)
    
    print(response['choices'][0]['text'])
    response = response['choices'][0]['text']

    tts = gtts.gTTS(text=response, lang='en')
    tts.save("response.mp3")
    os.system("start response.mp3")
