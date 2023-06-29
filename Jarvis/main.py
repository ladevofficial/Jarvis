# Import stuff
from datetime import datetime
import webbrowser
from AppOpener import open as appopener
from config import apikey
import openai
import os
from requests import get
import pywhatkit
from Features.GetPartOfDay import getPartOfday
from Features.TakeCommand import takeCommand
from Features.WindowsSpeak import say
from Features.Chat import chat
from Features.GetSitesList import getSitesList


# Do work using AI
def ai(prompt):
    openai.api_key = apikey 
    text = f"OpenAI response for Prompt: {prompt} \n **************** \n\n"

    respone = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt,
        temperature=0.7,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )

    text += respone["choices"][0]["text"]

    if not os.path.exists("OpenAI"):
        os.mkdir("OpenAI")

    with open(f"OpenAI/{''.join(prompt.split('AI')[1:]).strip()}.txt", "w") as f:
        f.write(text)

    say("Sir file created and stored in OpenAI folder.")


# Activated
def activated():
    hour = getPartOfday(datetime.now().hour)
    say(f"Good {hour} Sir. How may I help you?")

    while True:
        print("Listening...")
        query = takeCommand()

        # Open Stuff
        if "open".lower() in query.lower():
            isWebsite = False
            sites = getSitesList()
            
            for site in sites:
                if f"open {site[0]}".lower() in query.lower():
                    say(f"Opening {site[0]} Sir...")
                    webbrowser.open(site[1])
                    isWebsite = True

            if isWebsite != True:
                appName = ''.join(query.split('open')[1:]).strip()
                try:
                    appopener(appName.lower(), match_closest=True)
                    say(f"Opening {appName} Sir.")
                except:
                    say(f"Sir I was unable to find anything realted to {appName}.")
        
        # Say current time
        elif "time".lower() in query.lower():
            time = datetime.now().strftime("%I:%M %p")
            say(f"The time right now is {time}.")

        # Say current date
        elif "date".lower() in query.lower():
            date = datetime.now().strftime("%B %d, %Y")
            say(f"Sir today is {date}.")

        # Say current day
        elif "day".lower() in query.lower():
            day = datetime.now().strftime("%A")
            say(f"Sir today is {day}.")

        # Open cmd
        elif "open cmd".lower() in query.lower():
            say("Opening Command Prompt.")
            os.system("start cmd")

        # Get ip address
        elif "ip address".lower() in query.lower():
            ip = get('https://api.ipify.org').text
            say(f"Sir your IP Address is {ip}.")

        # Play songs on youtube
        elif "play song on youtube".lower() in query.lower():
            say("Sir which song to play on youtube.")
            print("Listening...")
            input = takeCommand()

            say(f"Playing {input} on youtube.")
            pywhatkit.playonyt(input)

        # Shutdown pc
        elif "shutdown".lower() in query.lower():
            say("Shutting down system.")
            os.system("shutdown /s /t 5")

        # Restart pc
        elif "restart".lower() in query.lower():
            say("Restarting the system.")
            os.system("shutdown /r /t 5")

        # Put pc to sleep
        elif "sleep".lower() in query.lower() and "system".lower() in query.lower():
            say("Putting the system to sleep.")
            os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")

        # Use AI to create prompts
        elif "using ai".lower() in query.lower():
            say("Ok Sir, creating file.")
            ai(prompt=query)

        # Deactivate jarvis
        elif "deactivate".lower() in query.lower() and "jarvis".lower() in query.lower():
            say("Deactivated.")
            deactivated()

        # Quit jarvis
        elif "quit".lower() in query.lower() and "jarvis".lower() in query.lower():
            say("Ok Sir. Quitting....")
            exit()

        # Bye jarvis
        elif "bye".lower() in query.lower() and "jarvis".lower() in query.lower():
            say("Bye. Have a nice day sir!")
            exit()

        # Goodnight jarvis
        elif "good night".lower() in query.lower() and "jarvis".lower() in query.lower():
            say("Goodnight Sir.")
            exit()

        # Reset chat
        elif "reset chat".lower() in query.lower() or "clear chat".lower() in query.lower():
            say("Chat reset!")
            chat().chatStr = ""

        # Chat with jarvis
        else:
            chat(query)


# Deactivated
def deactivated():
    while True:
        print("Deactivated...")
        input = takeCommand()

        # Activate jarvis
        if "activate".lower() in input.lower() and "jarvis".lower() in input.lower():
            activated()

        # Wakeup jarvis
        if "wake up".lower() in input.lower() and "jarvis".lower() in input.lower():
            activated()

        # Quit jarvis
        elif "quit".lower() in input.lower() and "jarvis".lower() in input.lower():
            say("Ok Sir. Quitting....")
            exit()

        # Bye jarvis
        elif "bye".lower() in input.lower() and "jarvis".lower() in input.lower():
            say("Bye. Have a nice day sir!")
            exit()

        # Goodnight jarvis
        elif "good night".lower() in input.lower() and "jarvis".lower() in input.lower():
            say("Goodnight Sir.")
            exit()


# Call on start
if "__name__ == '__main__'":
    deactivated()