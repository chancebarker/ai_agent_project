import os
import sys
import argparse
from google.genai import types
from dotenv import load_dotenv
from google import genai
from prompts import system_prompt
from call_function import available_functions, call_function

load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")

if api_key == None:
    raise RuntimeError("No API Key found. Look here https://www.boot.dev/lessons/3d695968-98c9-4a91-b1e2-0ca53e8826b7")

parser = argparse.ArgumentParser(description="Chatbot")
parser.add_argument("user_prompt", type=str, help="User prompt")
parser.add_argument("--verbose", action="store_true")

args = parser.parse_args()

messages = [types.Content(role="user", parts=[types.Part(text=args.user_prompt)])]


def main():
    client = genai.Client(api_key=api_key)

    for _ in range(20):
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=messages,
            config=types.GenerateContentConfig(
                tools=[available_functions],
                system_instruction=system_prompt,
                temperature=0,
            ),
        )

        # Add model's candidates to conversation history
        for candidate in response.candidates:
            messages.append(candidate.content)

        # If no function calls, we're done
        if not response.function_calls:
            print(f"Final response:\n{response.text}")
            return

        # Process function calls
        function_responses = []
        for fc in response.function_calls:
            function_call_result = call_function(fc, verbose=args.verbose)

            if not function_call_result.parts:
                raise Exception("No parts in function call result")
            if function_call_result.parts[0].function_response is None:
                raise Exception("No function response in result")
            if function_call_result.parts[0].function_response.response is None:
                raise Exception("No response in function response")

            function_responses.append(function_call_result.parts[0])

            if args.verbose:
                print(f"-> {function_call_result.parts[0].function_response.response}")

        # Add tool results to conversation
        messages.append(types.Content(role="user", parts=function_responses))

    print("Max iterations reached without a final response.")
    sys.exit(1)


main()