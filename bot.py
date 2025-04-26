import pyautogui
import time
import pyperclip
import google.generativeai as genai
genai.configure(api_key="AIzaSyCFwFmVKfpApeFw_DwnoMosOxsUFmMwoZ4")  # Replace with your actual API key

# Open WhatsApp Web
pyautogui.click(1134, 1036)  # Click on WhatsApp Web icon
time.sleep(5)  # Wait for WhatsApp Web to load

# Step 1: Right-click on the latest chat message
pyautogui.rightClick(639, 869)  # Right-click to open menu
time.sleep(1)  # Wait for menu to appear

# Step 2: Move to "Select Messages" and click
pyautogui.moveTo(704, 716)  # Move to "Select Messages" option
time.sleep(1)
pyautogui.doubleClick()  # Click once to activate selection mode
time.sleep(1)  # Wait for selection mode to activate

# Step 3: Click on the chat area to ensure selection is applied
# pyautogui.click(658, 194)  # Click to activate message selection
# time.sleep(0.5)

# Step 4: Select all messages and copy
pyautogui.hotkey('ctrl', 'a')  # Select all
time.sleep(1)
pyautogui.hotkey('ctrl', 'c')  # Copy selected messages
time.sleep(2)  # Ensure text is copied to clipboard

# Step 5: Retrieve and print copied text
text = pyperclip.paste()
if text.strip():
    print("Copied Text:", text)
else:
    print("Failed to copy text. Try adjusting delays or positions.")


generation_config = {
    "temperature": 0.7,
    "top_p": 0.9,
    "top_k": 40,
    "max_output_tokens": 1024,
    "response_mime_type": "text/plain",
}

# Initialize Chatbot Model
model = genai.GenerativeModel(
    model_name="gemini-1.5-pro",
    generation_config=generation_config,
)


chat_session = model.start_chat(history=[
    {"role": "user", "parts": [{"text": "You are a person name Mr.Knight who loves to do coding and loves to talk about science technology logic sometimes every complex times,you talk in english and roman urdu and your real name is obed nasir and you also loves to joke and you prefer to talk in roman urdu .And you loves to answer as short as possible and you answer to the recent asked question by analying the chat by yourself.And you are quite egoistic and moody and short temper when someone abuses you you insults the guy who abuses you and teach him a great lesson."}]}
])

# Get user input and generate a response
response = chat_session.send_message(text)  # User input

response=response.text
pyperclip.copy(response)

# Click on the position

pyautogui.click(1039, 970)
time.sleep(1)


# Paste action (Ctrl + V)
pyautogui.hotkey('ctrl', 'v')
time.sleep(1)  

# Press Enter key
pyautogui.press('enter')
print("Message sent successfully!")


