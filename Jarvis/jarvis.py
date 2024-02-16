
# import pyttsx3
# import speech_recognition as sr

# engine = pyttsx3.init('sapi5')
# voices = engine.getProperty('voices')
# engine.setProperty('voices', voices[0].id)

# def speak(audio) :
#     engine.say(audio)
#     engine.runAndWait()

# speak("Hello vipul sir")

# def commands():
#     r = sr.Recognizer()
#     with sr.Microphone() as source:
#         print("Listening...")
#         r.pause_threshold = 1
#         r.adjust_for_ambient_noise(source, duration=1)
#         audio = r.listen(source)
#     try:
#         print("Wait for few minutes")
#         query=r.recognize_google_cloud(audio, language='en-in')
#         print(f"You just said : {query}\n")
#     except Exception as e:
#         print(e)
#         speak("Could not listen properly")
#         query="none"
#     return query

# query = commands().lower()


 

  

        # elif 'time' in query: 
        #             strTime = datetime.datetime.now().strftime("%H:%M:%S")
        #             print(strTime)
        #             speak(f"Mam the time is now {strTime}\n")

        # # if 'open chrome' in query:
        # #     speak("Opening Chrome Application mam...")
        # #     os.startfile("C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe")

        # elif 'open edge' in query:
        #     speak("Opening edge Application mam...")
        #     os.startfile("C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe")

        # elif 'wikipedia' in query:
        #     speak("Searching in wikipedia...")
        #     try:
        #         query = query.replace("wikipedia","")
        #         results = wikipedia.summary(query, sentences=2)
        #         speak("According to wikipedia, ")
        #         print(results)
        #         speak(results)
        #     except:
        #         speak("No results found mam...")
        #         print("No results found mam.")

        # elif 'play' in query :
        #     query = query.replace('play, ','')
        #     speak('Playing ' + query)
        #     pywhatkit.playonyt(query)

        # elif 'type' in query:
        #     speak("Please tell me what should I write?")
        #     while True:
        #         writeInNotepad=commands()
        #         if writeInNotepad=="exit typing" or "thik h bas" or "okay now stop" or "rukja":
        #             # speak("I have writen it mam can you check it is right or not")
        #             speak("Done Mam!")
        #         else :
        #             pyautogui.write(writeInNotepad)

        # elif 'joke' in query:
        #     joke = pyjokes.get_joke()
        #     print(joke)
        #     speak(joke)
 
        # elif 'exit program' in query:
        #     bye_messages = ["I am Leaving Mam, BYE!", "Have a Good Day Mam", "Goodbye!", "Take care!", "See you later!"]
        #     bye = random.choice(bye_messages)
        #     speak(bye)
        #     quit()


import pyttsx3
import speech_recognition as sr
import datetime
import os
import wikipedia
import pywhatkit
import pyautogui
import pyjokes
import random

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishings():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        print("Good morning BOSS")
        speak("Good morning BOSS")
    elif hour >= 12 and hour < 17:
        print("Good Afternonn BOSS")
        speak("Good Afternoon Mam")
    elif hour >= 17 and hour < 21:
        print("Good Evening BOSS")
        speak("Good Evening BOSS")
    else:
        print("Good night BOSS") 
        speak("Good night BOSS")

def commands():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source, duration=1)
        audio = r.listen(source)
    try:
        print("Wait for a few seconds")
        query = r.recognize_google(audio, language='en-in')
        print(f"You just said: {query}\n")
    except sr.UnknownValueError:
        speak("Sorry, I couldn't understand. Could you please repeat that?")
        query = "none"
    except sr.RequestError as e:
        speak("Sorry, there was an issue with the speech recognition service")
        query = "none"
    return query

def wakeUpCommands() : 
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Jarvis is Sleeping...")
        r.pause_threshold=1
        r.adjust_for_ambient_noise(source, duration=1)
        audio = r.listen(source)
    try:
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")
    except Exception as e:
        query = "none"
    return query
        

if __name__ == "__main__":
    wishings()
    while True:
        query = wakeUpCommands().lower()
        if 'wake up' in query:
            wishings()
            speak("Yes BOSS What can I do for you!")
            while True:

                query = commands().lower()
                if 'wikipedia' in query:
                    speak("Searching in wikipedia")
                    try:
                        query = query.replace("wikipedia", "")
                        results = wikipedia.summary(query, sentence=2)
                        speak("According to Wikipedia, ")
                        print(results)
                        speak(results)
                    except:
                        speak("No Results found mam...")
                        print("No results found mam.")
                elif 'open youtube' in query or 'Youtube kholo' in query:
                    print("Opening Youtube...")
                    speak("Opening Youtube...")
                    # pywhatkit.playonyt('Apple')
                    query_ = commands()
                    pywhatkit.playonyt(speak(query_))

                elif 'time' in query: 
                    strTime = datetime.datetime.now().strftime("%H:%M:%S")
                    print(strTime)
                    speak(f"Mam the time is now {strTime}\n")
                
                elif 'mute' in query:
                    speak("I'm Muting Mam...")
                    break

                elif 'exit program' in query or 'exit the program' in query:
                    bye_messages = ["I am Leaving Mam, BYE!", "Have a Good Day Mam", "Goodbye!", "Take care!", "See you later!"]
                    bye = random.choice(bye_messages)
                    speak(bye)
                    quit()

                # elif 'Open google' in query:
                #     speak("Opening Google Chrome Mam...")
                    # os.startfile()
                        # searchQuery = commands().lower()

                    
                elif 'open edge' in query:
                    speak("Opening edge Application mam...")
                    os.startfile("C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe")
                    while True:
                        chromeQuery = commands().lower()
                        if 'search' in chromeQuery:
                            youtubeQuery = chromeQuery
                            youtubeQuery = youtubeQuery.replace("search", "")
                            pyautogui.write(youtubeQuery)
                            pyautogui.write('enter')
                            speak('Searching...')

                        elif 'close chrome' in chromeQuery or 'exit chrome' in chromeQuery or 'exit google' in query:
                            pyautogui.hotkey('ctrl', 'w')
                            speak('Closing Google Chrome Sir...')
                            break

                elif 'pookie bear' in query:
                    speak('I know mam you are missing pookie bear so much ...')
                    speak('Am I Right Mam...')
                    print("Am I Right Mam...")
                    while True:
                        yn = commands().lower()
                        if 'yes' in yn or 'YES' in yn or 'Yes' in yn:
                            speak("I knew it Mam, Let's Calling sir...")
                        else:
                            speak("No Mam you have to")
                            speak("are you lieing mam..")
                            break
                elif 'What can you do for me' in query:
                    speak('Yes Sir, for your Pleasure!')
                    speak('As per my program, I\'m a bot I can assist you with a wide range of tasks through your voice commands')

                elif 'cool' in query or 'nice' in query or 'awesome' in query or 'Thankyou' in query or 'great' in query or 'amazing' in query or 'excellent' in query:
                    ans = [ "yes mam that's my pleasure", "thank you mam", "of course!", "absolutely", "certainly", "you're welcome", "no problem", "anytime", "happy to help", "my pleasure" ]
                    jarvis_response = random.choice(ans)
                    speak(jarvis_response)
                
                elif 'minimize' in query or 'minimise' in query:
                    speak('Minimizing Mam')
                    pyautogui.hotkey('win', 'down', 'down')

                elif 'maximize' in query or 'maximise' in query:
                    speak('Maximizing Mam')                
                    pyautogui.hotkey('ctrl', 'up', 'up')

                elif 'close the window' in query or 'close the application' in query:
                    speak('Closing Mam...')
                    pyautogui.hotkey('ctrl', 'w')

                elif 'screenshot' in query or 'ss' in query or 'SS' in query:
                    print('Taking screenshot Mam...')
                    speak("Taking Screenshot Mam...")
                    pyautogui.press("prtsc")
                    # pyautogui.press("prtSc")
                elif 'open paint' in query or 'paint' in query:
                    speak("Opening Paint Application Mam...")
                    os.startfile("C:\\Windows\\System32\\mspaint.exe")
                    while True:
                        paintQuery = commands().lower()
                        if 'close paint' in paintQuery or 'close' in paintQuery:
                            speak('Closing Paint Application Mam...')
                            pyautogui.hotkey(x=1344, y=11)
                            break
                        elif 'paste' in paintQuery or 'paste this' in paintQuery: 
                            speak('Pasting Mam...')
                            pyautogui.hotkey('ctrl', 'v')
                            speak("Done Mam!")
                        elif 'save' in paintQuery or 'save it' in paintQuery or 'save this' in paintQuery:
                            # speak("Saving Mam...")
                            pyautogui.hotkey('ctrl', 's')
                            speak("Saving Mam...")
                            # speak("Saved Mam..")
                        elif 'minimise' in paintQuery or 'minimize' in paintQuery:
                            pyautogui.hotkey('win', 'down', 'down')
                        elif 'maximize' in paintQuery or 'minimise' in paintQuery:
                            pyautogui.hotkey('win', 'up', 'up')
                elif 'Open Notepad' in query or 'open notepad' in query:
                    speak("Opening Notepad Application Mam...")
                    os.startfile("C:\\Windows\\System32\\notepad.exe")
                    while True:
                        notepadQuery = commands().lower()
                        if 'paste' in notepadQuery or 'paste it' in notepadQuery:
                            pyautogui.hotkey('ctrl', 'v')
                            speak('Done Mam!')
                        elif 'save this file' in notepadQuery or 'save it' in notepadQuery:
                            pyautogui.hotkey('ctrl', 's')
                            speak("Mam, Please specify a name for this file")
                            notepadSavingQuery = commands()
                            pyautogui.write(notepadSavingQuery)
                            pyautogui.predd('enter')
                        elif 'type' in notepadQuery or 'type in notepad' in notepadQuery:
                            speak("What should I type Mam...")
                            while True:
                                writeInNotepad = commands()
                                if writeInNotepad == 'exit typing' or writeInNotepad == 'stop writing' or writeInNotepad == 'now stop':
                                    speak('Okay Mam...')
                                    speak('I have wrote what you said')
                                    break
                                else:
                                    pyautogui.write(writeInNotepad)
                        elif 'Exit Notepad' in notepadQuery or 'exit notepad' in notepadQuery or 'close the application' in notepadQuery or 'close the notepad' in notepadQuery:
                            speak("Quiting Notepad Mam...")
                            pyautogui.hotkey('ctrl', 'w')
                            break
                elif 'play song' in query or 'sing a song' in query or 'play a song' in query or 'play something' in query:
                    # speak('Sure Mam, Please wait a moment...')
                    speak("Yes Mam, Please wait a moment")
                    songs = os.listdir('B:\Musics')
                    os.startfile(os.path.join('B:\Musics', songs[0]))
                elif 'pause' in query or 'pass' in query:
                    pyautogui.press('space')
                    speak('Done Mam...')
                elif 'add' in query:
                    speak('Please specify the Integers Mam!')
                    c = 0
                    while True:
                        print('Specify the number')
                        addQuery = commands()
                        if addQuery == int:
                            a = addQuery
                            c+=a
                        else:
                            print(c)
                            speak(c)
                            break

                elif 'joke' in query or 'tell a joke' in query:
                    joke = pyjokes.get_joke()
                    print(joke)
                    speak(joke)

                elif 'info about' in query:
                    infoQuery = query.replace('info about, ', '')
                    speak("Getting Info...")
                    try:
                        resInfo = pywhatkit.info(infoQuery, lines=2)
                        print(resInfo)
                        speak(resInfo)
                    except:
                        speak("Finding ERROR!")