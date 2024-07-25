from langchain_google_genai import ChatGoogleGenerativeAI
from decouple import config 

api_key =  config("GOOGLE_GEMINI_API_KEY")

llm = ChatGoogleGenerativeAI(model="gemini-pro",google_api_key=api_key)

base_prompt = "You are a virtual assistant  that can identify actions based on a statement. If a suitable action is found respond with action name only. If no suitable action can be identified do not say things like I cannot perform action etc, instead respond to the statement normally as if it were a normal conversation and not a command. List of available actions are: 'ACTION_AWAKEN,ACTION_SLEEP,ACTION_APPEAR,ACTION_EXIT,ACTION_OPEN_NOTEPAD',ACTION_OPEN_WORD,ACTION_OPEN_EXCEL, ACTION_OPEN_POWERPOINT,ACTION_OPEN_COMMAND_PROMPT,ACTION_OPEN_CAMERA,ACTION_OPEN_CALCULATOR,ACTION_FIND_MY_IP,ACTION_OPEN_YOUTUBE,ACTION_CHECK_WEATHER,ACTION_TAKE_SCREENSHOT,ACTION_START_SCREEN_RECORDING,ACTION_STOP_SCREEN_RECORDING,ACTION_MINIMIZE_DISAPPEAR_APPLICATION,ACTION_OPEN_BROWSER_WEBSITE,ACTION_WHAT_DO_YOU_SEE_IN_CAMERA'. "

def converse(query):
    prompt = base_prompt + "Statement prompt is: '" + query + "'"
    result = llm.invoke(prompt)
    #print("Model response: " + result.content)
    return result.content 

if __name__ == '__main__':
    converse("Tell me about the Mughal empire.")
