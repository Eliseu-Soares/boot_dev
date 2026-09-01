import os
from dotenv import load_dotenv
from openai import OpenAI
import argparse

load_dotenv()
api_key = os.environ.get("OPENROUTER_API_KEY")



client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=api_key,
)






def main():
    parser = argparse.ArgumentParser(description="Chatbot")
    parser.add_argument("user_prompt", type=str, help="User Prompt")
    parser.add_argument("--verbose", action="store_true", help="Enable verbose output")
    args = parser.parse_args()

    message = [
    {
        "role": "user",
        "content": args.user_prompt,
    }
]

    completion = client.chat.completions.create(
    model="openrouter/free",
    messages=message
    )
    if args.verbose:
        print(f"User prompt: {args.user_prompt}")
        print(f"Prompt tokens: {completion.usage.prompt_tokens}")
        print(f"Response tokens: {completion.usage.completion_tokens}")
    print(f"Assistent: {completion.choices[0].message.content}")

if __name__ == "__main__":
    main()
