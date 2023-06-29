import openai
from config import apikey
from Features.WindowsSpeak import say

chatStr = ""
def chat(prompt):
    global chatStr

    openai.api_key = apikey 

    chatStr += f"Sir: {prompt} \n Jarvis: "
    respone = openai.Completion.create(
        model="text-davinci-003",
        prompt=chatStr,
        temperature=0.7,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )

    say(respone['choices'][0]['text'])
    chatStr += f"{respone['choices'][0]['text']} \n"
    return respone["choices"][0]["text"]