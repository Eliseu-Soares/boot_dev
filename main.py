import os
import json
from dotenv import load_dotenv
from openai import OpenAI
import argparse
from prompts import system_prompt
from call_function import  available_functions, call_function
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

    msg = [
        {
            "role": "system",
            "content": system_prompt
        },
        {
            "role": "user",
            "content": args.user_prompt,
        }
    ]
    for _ in range(20):
        completion = client.chat.completions.create(
        model="openrouter/free",
        messages=msg,
        tools=available_functions
        )

        if args.verbose:
            print(f"User prompt: {args.user_prompt}")
            print(f"Prompt tokens: {completion.usage.prompt_tokens}")
            print(f"Response tokens: {completion.usage.completion_tokens}")
        print(f"Assistent: {completion.choices[0].message.content}")
        message = completion.choices[0].message
        msg.append(message)
        if not message.tool_calls:
            print("Final response:")
            print(message.content)
            return
        if message.tool_calls:
                for v in message.tool_calls:
                    result_message = call_function(v, args.verbose)
                    if not result_message["content"]:
                        raise ValueError("Function returned empty content")
                    if args.verbose:
                        print(f'-> {result_message["content"]}')
                    msg.append(result_message)
        else:
            print("Reached the maximum number of iterations")
            exit(0)
if __name__ == "__main__":
    main()
