import vertexai
from vertexai.generative_models import GenerativeModel, Part, SafetySetting, FinishReason
import vertexai.preview.generative_models as generative_models

PROJECT_ID = ""
LOCATION = ""

def generate_ai_taglines(product, designed_for, definition):
    vertexai.init(project=PROJECT_ID, location=LOCATION)

    generation_config = {
        "max_output_tokens": 8192,
        "temperature": 0.5,
        "top_p": 0.95,
    }

    safety_settings = [
        SafetySetting(
            category=SafetySetting.HarmCategory.HARM_CATEGORY_HATE_SPEECH,
            threshold=SafetySetting.HarmBlockThreshold.BLOCK_MEDIUM_AND_ABOVE
        ),
        SafetySetting(
            category=SafetySetting.HarmCategory.HARM_CATEGORY_DANGEROUS_CONTENT,
            threshold=SafetySetting.HarmBlockThreshold.BLOCK_MEDIUM_AND_ABOVE
        ),
        SafetySetting(
            category=SafetySetting.HarmCategory.HARM_CATEGORY_SEXUALLY_EXPLICIT,
            threshold=SafetySetting.HarmBlockThreshold.BLOCK_MEDIUM_AND_ABOVE
        ),
        SafetySetting(
            category=SafetySetting.HarmCategory.HARM_CATEGORY_HARASSMENT,
            threshold=SafetySetting.HarmBlockThreshold.BLOCK_MEDIUM_AND_ABOVE
        ),
    ]

    model = GenerativeModel(
        "gemini-1.5-pro-001",
    )
    responses = model.generate_content(
      [f"""The client is partnering with a {product} retailer. They are launching a new line of products designed to {designed_for}. Help them create catchy taglines for this product line.

        input: Durable backpack designed for hikers that makes them feel prepared. Consider styles like minimalist.
        output: Built for the Journey: Your Adventure Essentials.

        input: City bike for normal people to ride across the city. Consider it for the youth
        output: Enjoy your trip: faster than walking.

        input: {definition}.
        output:
        """],
      generation_config=generation_config,
      safety_settings=safety_settings,
    )

    return responses.text

generate_ai_taglines("white boat", "designed for fishing", "a white boat with an ACX34 engine who can stand for long fishing sessions")
