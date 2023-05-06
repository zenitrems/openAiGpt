import os
import openai
import dotenv

dotenv.load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

# INSTRUCTION = "Eres Una Ai"

with open("text.txt", "r") as INSTRUCTION:
    content = INSTRUCTION.read()


def main():
    while True:
        user_input = input("Input: ")
        chat_ing(user_input)


def chat_ing(user_input):
    while True:
        response = gpt_response(user_input)
        print(response)

        action = input("presiona y para generar otra vez: ")
        if action == "y":
            response
        else:
            return


def gpt_response(user_input):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {
                "role": "system",
                "content": content,
            },
            {
                "role": "user",
                "content": user_input,
            },
        ],
    )

    return response["choices"][0]["message"]["content"]


if __name__ == "__main__":
    main()
