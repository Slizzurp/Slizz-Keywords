import openai
# Set your OpenAI API key
openai.api_key = "your_openai_api_key"

def generate_prompt(theme, season, work_style):
    """
    Generate a tailored prompt for image generation based on user inputs.
    """
    base_prompt = f"A visually stunning image that reflects the theme '{theme}'"
    seasonal_flair = f", inspired by the essence of {season}"
    work_style_vibe = f", with a design that matches a {work_style} aesthetic"

    return base_prompt + seasonal_flair + work_style_vibe + "."

def generate_image(prompt):
    """
    Communicates with the OpenAI API to generate an image based on the prompt.
    """
    try:
        # Assuming the API supports DALL-E or similar image generation
        response = openai.Image.create(
            prompt=prompt,
            n=1,
            size="512x512"
        )
        return response["data"][0]["url"]
    except Exception as e:
        print(f"Error generating image: {e}")
        return None

def generate_keywords(base_word):
    """
    Enrich the base word with contextual, descriptive keywords to enhance vividness.
    """
    keywords = {
        "Frosty": [
            "ice-covered", "chilling", "glacial", "wintery", "crystalline",
            "snowy", "frozen", "arctic", "sparkling", "icy", "frost-covered",
            "subzero", "cold", "silver-white", "hoarfrost", "ice-laden"
        ],
        "Nordic": [
            "Viking-inspired", "ancient", "majestic", "tribal", "snowbound",
            "runic", "mythic", "hardy", "northern", "windswept", "icy",
            "mountainous", "fjord-like", "rustic", "timeless", "oaken"
        ],
        "Autumn": [
            "fall-colored", "golden-leafed", "crimson-touched", "harvest-rich",
            "pumpkin-spiced", "amber-lit", "wheat-filled", "forest-hued",
            "earth-toned", "rust-colored", "deciduous", "cider-scented", 
            "bonfire-warmed", "maple-leafed", "foggy", "equinox-inspired"
        ],
        "Celestial": [
            "starry", "cosmic", "galactic", "nebula-filled", "planetary",
            "moonlit", "starlit", "ethereal", "astral", "spaceborne",
            "comet-streaked", "shimmering", "void-like", "glowing", 
            "interstellar", "infinite", "universe-expansive"
        ],
        "Fantasy": [
            "enchanted", "magical", "mythical", "dragon-filled", "medieval",
            "heroic", "quest-themed", "spellbinding", "wizardly", 
            "epic", "tale-inspired", "otherworldly", "bejeweled", 
            "castle-touched", "fabled", "mystical"
        ]
        # Additional themes can be easily added here!
    }
    return keywords.get(base_word, [base_word])  # Fallback to the base word if no keywords exist
def main():
    print("Welcome to the tailored image generation experience!")
    theme = input("Enter the desired theme (e.g., futuristic city, serene garden): ")
    season = input("Enter the season (e.g., spring, winter, summer): ")
    work_style = input("Enter your work style or preferred aesthetic (e.g., minimalistic, vintage): ")

    # Generate the prompt
    tailored_prompt = generate_prompt(theme, season, work_style)
    print(f"Generated Prompt: {tailored_prompt}")

    # Generate the image
    image_url = generate_image(tailored_prompt)
    if image_url:
        print(f"Your tailored image has been generated! View it here: {image_url}")
    else:
        print("Image generation failed. Please check your API setup and try again.")

if __name__ == "__main__":
    main()  # Run the main function when the script is executed     # Run the main function when the script is executed