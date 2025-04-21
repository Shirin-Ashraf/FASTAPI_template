# app/models/gen_text_generator.py

def generate_text(prompt: str) -> str:
    """A very basic text generator logic (mock)"""
    if not prompt.strip():
        return "Please enter a valid prompt."
    
    return f"{prompt.strip()}... and then something amazing happened!"
