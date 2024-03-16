import speech_recognition as sr

levels = {

    "easy": ["dairy", "mouse", "computer"],

    "medium": ["programming", "algorithm", "developer"],

    "hard": ["neural network", "machine learning", "artificial intelligence"]

}

def start_game(level):
    words = levels[level]
    ans = ' '

    for word in words:
        s = 0
        while word not in ans and s != 3:
            ans = voice_recognition(word)
            s += 1
        else:
            if word in ans:
                print('Correct!')
        

recognizer = sr.Recognizer()

def voice_recognition(word):
    try:
        with sr.Microphone() as mic:
            print(f"Say {word}.")
            recognizer.adjust_for_ambient_noise(mic, duration=0.05, )
            audio = recognizer.listen(mic)

            text = recognizer.recognize_google(audio, language="en-EN")
            text = text.lower()
            
            print(text)

        return text

    except:
        print("Voice is not recognize")
        return ' '

theLevel = input().lower()
start_game(theLevel)
