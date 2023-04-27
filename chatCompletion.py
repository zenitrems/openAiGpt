import os
import openai
import dotenv

dotenv.load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")


def gpt3Chat():
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {
                "role": "system",
                "content": systemRole,
            },
            {
                "role": "user",
                "content": userRole,
            },
        ],
        temperature=0.7,
        n=1,
        stop=None,
    )
    return print(response["choices"][0]["message"]["content"])


systemRole = input("System Content:")
userRole = input("User Content:")

gpt3Chat()
do = input("Preguntar de nuevo? (y/n):")
while do == "y":
    systemRole = input("System Content:")
    userRole = input("User Content:")
    gpt3Chat()
    do = input("Preguntar de nuevo? (y/n):")
