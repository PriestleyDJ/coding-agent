import os
import sys
from dotenv import load_dotenv
from google import genai

def main():
    # Load environment variables
    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")

    # Create a new instance of Gemini client
    client = genai.Client(api_key=api_key)

    try:
        user_prompt = sys.argv[1]
    except IndexError:
        print("ERROR: Command line prompt should not be empty!")
        sys.exit(1)

    response = client.models.generate_content(
        model="gemini-2.0-flash-001", 
        contents=user_prompt,
    )

    print(response.text)
    print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
    print(f"Response tokens: {response.usage_metadata.candidates_token_count}")


if __name__ == "__main__":
    main()
