from langchain_core.messages import HumanMessage
from langchain_google_genai import ChatGoogleGenerativeAI
from decouple import config 

api_key = config("GOOGLE_GEMINI_API_KEY")
vision_model = ChatGoogleGenerativeAI(model="gemini-pro-vision", google_api_key=api_key)
screenshot_file = config("MEDIA_DIR") + "/" + config("SCREENSHOT_FILE")

def describe_image():
    message = HumanMessage(
        content=[
            {
                "type": "text",
                "text": "This is image of a video feed. Describe only what you see in it, and absolutely nothing else."
            },
            {"type": "image_url", "image_url": screenshot_file}
        ]
    )

    result = vision_model.invoke([message])
    print(result.content)
    return result.content 

if __name__ == '__main__':
    describe_image()
