import base64
import vertexai
from vertexai.generative_models import GenerativeModel, Part, FinishReason
import vertexai.preview.generative_models as generative_models
import base64
from PIL import Image
import io

# Function to convert image to base64 string
def image_to_base64(image_path):
    # Open the image file
    with Image.open(image_path) as image:
        # Convert image to bytes
        buffered = io.BytesIO()
        image.save(buffered, format="JPEG")
        image_bytes = buffered.getvalue()
        
        # Encode bytes to base64 string
        base64_string = base64.b64encode(image_bytes).decode('utf-8')
        return base64_string

# Example usage



def generate():
    vertexai.init(project="qualified-cedar-405007", location="us-central1")
    model = GenerativeModel(
        "gemini-1.5-pro-001",
    )
    responses = model.generate_content(
        [image1, f"{file} using this html markdown and the image provided give me structured text output"],
        generation_config=generation_config,
        safety_settings=safety_settings,
        stream=True,
    )
    output = ""
    for response in responses:
        output += response.text

    return output


for i in range(0,2):
        
    with open(f"screenshot_{i}.txt","r") as f:
        file = f.read()
    image_path = f'screenshot_{i}.png'
    base64_string = image_to_base64(image_path)

    image1 = Part.from_data(
        mime_type="image/png",
        data=base64.b64decode(base64_string
    ))

    generation_config = {
        "max_output_tokens": 8192,
        "top_p": 0.95,
    }

    safety_settings = {
        generative_models.HarmCategory.HARM_CATEGORY_HATE_SPEECH: generative_models.HarmBlockThreshold.BLOCK_MEDIUM_AND_ABOVE,
        generative_models.HarmCategory.HARM_CATEGORY_DANGEROUS_CONTENT: generative_models.HarmBlockThreshold.BLOCK_MEDIUM_AND_ABOVE,
        generative_models.HarmCategory.HARM_CATEGORY_SEXUALLY_EXPLICIT: generative_models.HarmBlockThreshold.BLOCK_MEDIUM_AND_ABOVE,
        generative_models.HarmCategory.HARM_CATEGORY_HARASSMENT: generative_models.HarmBlockThreshold.BLOCK_MEDIUM_AND_ABOVE,
    }

    text = generate()
    with open(f"text{i}.txt","w") as f:
        f.write(text)

    print(f"text{i}.txt created")
