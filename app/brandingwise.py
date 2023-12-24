
from openai import OpenAI
import argparse
import re

# Memuat variabel lingkungan dari file .env
client = OpenAI(api_key="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")

# system_message = {"role": "system", "content": "You are a poetic assistant, skilled in explaining complex programming concepts with creative flair."}
# prompt = " coppy"
MAX_INPUT_LENGTH = 15

def main():
    print("Running Copy Kitt!")
    
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--input", required=True)
    args = parser.parse_args()
    user_input = args.input
    print(f"User input: {user_input}")
    
    if validate_length(user_input):
        generate_branding_snippet(user_input)
        generate_keyswords(user_input)
        
    else:
        raise ValueError(
            f"Input length is too long. Must be under {MAX_INPUT_LENGTH}. Submitted input is {user_input}"
        )    


def validate_length(prompt: str) -> bool:
    return len(prompt) <= MAX_INPUT_LENGTH

def generate_keyswords(promt: str) -> list[str]:
    response = {"role": "user", "content": "Generate related branding keywords for {prompt}: "}
    
    ENGINE = "gpt-3.5-turbo"
    completion = client.chat.completions.create(
    model= ENGINE,
    max_tokens = 20,
    messages=[response]
    )
    
    keywords_messege = completion.choices[0].message
    keywords_text = keywords_messege.content
    role = keywords_messege.role
    
    keywords_text = keywords_text.strip()
    # keywords_array = re.split(r',\s*|\n|\s*;\s*|\s*-\s*', keywords_text)
    # keywords_array = [k.lower().strip() for k in keywords_array if k.strip()]
    
    keywords_array = re.split(",|\n|;|-", keywords_text)
    keywords_array = [k.lower().strip() for k in keywords_array]
    keywords_array = [k for k  in keywords_array if len(k) > 0] 
    
    print(f"Keywords: {keywords_array}")

    return keywords_array

def generate_branding_snippet(prompt: str) :
    response = {"role": "user", "content": "Generate upbeat branding snippet for {prompt}: "}

    ENGINE = "gpt-3.5-turbo"
    completion = client.chat.completions.create(
    model= ENGINE,
    max_tokens = 20,
    messages=[response]
    )

    branding_message = completion.choices[0].message
    branding_text = branding_message.content
    role = branding_message.role
    
    if not branding_text.endswith(('.', '!', '?')):
        branding_text += "..."

    print(f"Snippet: {branding_text}")
    
    return branding_text
     
if __name__ == "__main__":
    main()
