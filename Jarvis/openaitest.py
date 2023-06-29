from config import apikey
import openai

openai.api_key = apikey
response = openai.Completion.create(
  model="text-davinci-003",
  prompt="What is your name",
  temperature=0.7,
  max_tokens=256,
  top_p=1,
  frequency_penalty=0,
  presence_penalty=0
)
print(response)
print(response["choices"][0]["text"])