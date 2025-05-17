# ai_helper.py

import os
from openai import OpenAI, RateLimitError, AuthenticationError

# Load the API key from environment variable
api_key = os.getenv("OPENAI_API_KEY")

# Initialize the OpenAI client
client = OpenAI(api_key=api_key)

async def get_task_suggestions(prompt: str):
    try:
        response = await client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "user", "content": f"Suggest 3 tasks related to: {prompt}"}
            ]
        )
        return [choice.message.content.strip() for choice in response.choices]

    except RateLimitError:
        print("⚠️ Rate limit or quota exceeded. Check your usage at https://platform.openai.com/account/usage.")
        return []

    except AuthenticationError:
        print("❌ Invalid API key. Please check your API key in your environment or config.")
        return []

    except Exception as e:
        print(f"❗ An unexpected error occurred: {e}")
        return []
