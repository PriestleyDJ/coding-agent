import os
import argparse
from dotenv import load_dotenv
from google import genai
from google.genai import types
from call_functions import available_functions
from prompts import system_prompt

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

# Generate response
response = client.models.generate_content(
    model="gemini-2.0-flash-001",
    contents=messages,
    config=types.GenerateContentConfig(
        tools=[available_functions], system_instruction=system_prompt
    ),
)

if args.verbose:
    print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
    print(f"Response tokens: {response.usage_metadata.candidates_token_count}")
    print(f"User prompt: {user_prompt}")

if response.function_calls:
    for function in response.function_calls:
        print(f"Calling function: {function.name}({function.args})")
else:
    print(f"Response: {response.text}")
