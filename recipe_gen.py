import anthropic
import os
from dotenv import load_dotenv

load_dotenv()

client = anthropic.Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))

def generate_recipes(ingredients: list) -> str:
    if not ingredients:
        return "No food detected. Try a clearer photo."

    ingredient_list = ", ".join(ingredients)

    prompt = f"""
You are a friendly chef assistant.
The user has these ingredients: {ingredient_list}

Suggest 3 recipes they can make. For each recipe:
1. Give it a fun name with emoji
2. List which ingredients it uses
3. Give 4-5 simple cooking steps
4. Mention total cooking time
"""

    message = client.messages.create(
        model="claude-opus-4-5",
        max_tokens=1024,
        messages=[{"role": "user", "content": prompt}]
    )

    return message.content[0].text