import speech_recognition as sr
import pyttsx3
import os
import time


def speak(command):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty("voice","nepali")
    engine.say(command)
    engine.runAndWait()


def data_processing(usr_input):
    try:
        fp = open("Conversations.txt","r")
        for line in fp.readlines():
            quest, reply = line.split('-')
            if usr_input == quest:
                convert_text = reply
        fp.close()
        return convert_text
    except UnboundLocalError:
        return "Sorry! could you repeat that?\n"


def input_for_audio():
    r = sr.Recognizer()
    try:
        with sr.Microphone() as source2:
            r.adjust_for_ambient_noise(source2, duration=0.2)
            audio2 = r.listen(source2)
            text = r.recognize_google(audio2)
            text = text.lower()
            return text

    # except sr.RequestError as e:
    #     print("Error!")
        
    # except sr.UnknownValueError:
    #     print("Error!")
    except Exception:
        print("Error!")


def exit_sequence():
    i = 3
    while i >=1:
        os.system("clear")
        print(f"\n\n\n\t\t\t    Exiting in {i} secs...")
        i-=1
        time.sleep(1)
    os.system("clear")


def info():
    print("""
    About the program:

                This simple python script tries to have a normal conversation
                with the user. Although, it's still in development phase and
                requires much improvement.
            

    [Options]
    ->"text" or 't'         --for text interface
    ->"audio" or 'a'        --for audio interface
    ->"exit"                --for exiting program[while selecing interface]
    ->"Ctrl+C"              --for exiting program[while inside interface]
    """)


while True:
    
    os.system("clear")
    info()
    interface = input("Select user interface: ")
    if interface == "text" or interface == "t" or interface == "audio" or interface == "a" or interface == "exit":
        break
    else:
        print("Wrong Input!")
        time.sleep(1)


while True:  
    if interface == "text" or interface == 't':
        try:
            print(data_processing(input("Write something: ")))
        except KeyboardInterrupt:
            exit_sequence()
            break
    elif interface == "audio" or interface == 'a':
        try:
            speak(data_processing(input_for_audio()))
        except KeyboardInterrupt:
            exit_sequence()
            break
    elif interface == "exit":
        exit_sequence()
        break
