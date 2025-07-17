import os
import argparse
from dotenv import load_dotenv
from google import genai
from google.genai import types
from call_functions import available_functions, call_function
from prompts import system_prompt

def main()
    # Load environment
    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")
    client = genai.Client(api_key=api_key)

    # Check for arguments
    parser = argparse.ArgumentParser(description="AI Coding Assistant")
    parser.add_argument("user_prompt", help="Your prompt for the AI Coding Assistant")
    parser.add_argument(
        "-v", "--verbose", help="A more verbose output", action="store_true"
    )
    args = parser.parse_args()
    user_prompt = args.user_prompt

    # Message history
    messages = [
        types.Content(role="user", parts=[types.Part(text=user_prompt)]),
    ]

    generate_content(client, messages, args.verbose)

def generate_content(client, messages, verbose):
    # Generate response
    response = client.models.generate_content(
        model="gemini-2.0-flash-001",
        contents=messages,
        config=types.GenerateContentConfig(
            tools=[available_functions], system_instruction=system_prompt
        ),
    )

    if verbose:
        print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
        print(f"Response tokens: {response.usage_metadata.candidates_token_count}")
        print(f"User prompt: {user_prompt}")

    if not response.function_calls:
        return response.text

    function_responses = []
    for function_call_part in response.function_calls:
        function_call_result = call_function(function_call_part, verbose)
        if (
            not function_call_result.parts or not function_call_result.parts[0].function_response
        ):
            raise Exception("empty function call result")
        if verbose:
            print(f"-> {function_call_result.parts[0].function_response.response}")
        function_responses.append(function_call_result.parts[0])

    if not function_responses:
        raise Exception("no function responses generated, exiting.")


if __name__ == "__main__":
    main()
