print("\nHi! Welcome to joeyunderwood.com\n")
text_prompt = str(input("What would you like to see? "))

# dont hardcode this shit
api_key = "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"

import openai
openai.api_key = api_key

#openai.Model.list()  - prints list of all models
result_link = openai.Image.create(
    prompt = text_prompt,
    n = 1,
    size = "256x256"
)

print(result_link)
print("\n The end!")