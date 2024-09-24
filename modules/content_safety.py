from groq import Groq

def interpret_safety_check(raw_output):
    lines = raw_output.strip().split('\n')
    if lines[0].lower() == 'safe':
        return "The content appears to be safe."
    elif lines[0].lower() == 'unsafe':
            return f"The content may be unsafe."
    else:
        return f"{raw_output}. Please review manually."
    
def check_content_safety(image_description, api_key):
    client = Groq(api_key=api_key)

    try:
        chat_completion = client.chat.completions.create(
            messages=[
                {"role": "user", "content": f"{image_description}"},
            ],
            model="llama-guard-3-8b",
        )
        return interpret_safety_check(chat_completion.choices[0].message.content)
    except Exception as e:
        return f"Error during content safety check: {str(e)}"