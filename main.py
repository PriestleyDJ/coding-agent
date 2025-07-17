import os
import argparse
from dotenv import load_dotenv
from google import genai
from google.genai import types

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
)

if args.verbose:
    print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
    print(f"Response tokens: {response.usage_metadata.candidates_token_count}")
    print(f"User prompt: {user_prompt}")

print(f"Response: {response.text}")
