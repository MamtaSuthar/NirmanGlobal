import google.generativeai as genai
from decouple import config

# Configure Gemini API
genai.configure(api_key=config("GEMINI_API_KEY"))

# Initialize model
model = genai.GenerativeModel("gemini-1.5-flash")


# 🔹 Ask Gemini directly
def ask_gemini(message):
    try:
        response = model.generate_content(message)
        return response.text if response.text else "No response from AI."
    except Exception as e:
        return f"Error: {str(e)}"


# 🔹 Generate structured AI response
def generate_ai_response(message):
    prompt = f"""
    A user asked about interior design:
    "{message}"

    Give helpful interior design suggestions in simple points.
    """

    try:
        response = model.generate_content(prompt)
        return response.text if response.text else "No response generated."
    except Exception as e:
        return f"Error: {str(e)}"


# 🔹 Detect category of message
def detect_category(message):
    message = message.lower()

    if any(word in message for word in ["price", "cost", "budget"]):
        return "pricing"
    elif any(word in message for word in ["design", "interior", "decor"]):
        return "design"
    elif any(word in message for word in ["bad", "issue", "complaint"]):
        return "complaint"
    return "general"


# 🔹 Rule-based room design generator (no AI)
def generate_room_design(room_type, budget, style):
    room_type = room_type.lower()
    style = style.lower()
    budget = budget.lower()

    response = f"✨ {style.title()} {room_type.title()} Design Suggestions:\n\n"

    # Room logic
    if room_type == "bedroom":
        response += "• Use warm lighting for a cozy feel\n"
        response += "• Add wooden textures for comfort\n"

    elif room_type == "kitchen":
        response += "• Use modular cabinets for efficiency\n"
        response += "• Add under-cabinet lighting\n"

    elif room_type == "living room":
        response += "• Choose a statement sofa\n"
        response += "• Add wall art for personality\n"

    # Style logic
    if style == "modern":
        response += "\n• Stick to neutral colors like white, grey\n"
        response += "• Minimal furniture, clean lines\n"

    elif style == "luxury":
        response += "\n• Use marble or glossy finishes\n"
        response += "• Add gold/metal accents\n"

    elif style == "minimal":
        response += "\n• Declutter space\n"
        response += "• Use soft tones and simple decor\n"

    # Budget logic
    if budget == "low":
        response += "\n• Use laminate instead of wood\n"
        response += "• DIY decor elements\n"

    elif budget == "high":
        response += "\n• Invest in premium furniture\n"
        response += "• Custom lighting design\n"

    return response