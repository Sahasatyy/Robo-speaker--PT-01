import pyttsx3

def robo(word):
    engine = pyttsx3.init()
    engine.say(word)
    engine.runAndWait()

if __name__ == "__main__":
    print("Robo speaker 1.1")
    while True:
        word = input("Enter the word you want robo to pronounce: ")
        if word == "q":
            break
        robo(word)