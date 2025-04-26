import google.generativeai as genai

# Configure API Key
genai.configure(api_key="AIzaSyCFwFmVKfpApeFw_DwnoMosOxsUFmMwoZ4")  # Replace with your actual API key

# Create the model
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
chat="""

[1/14/2025 7:45 PM] Mr. Knight: https://www.instagram.com/reel/DEFQG5gzhgc/?igsh=MWZyZjZmNGF6aWpzbA==
[1/16/2025 12:08 AM] Mr. Knight: https://www.instagram.com/reel/DEgxIx5NW9_/?igsh=MWR2eHhsYngzdm1kdA==
[2/8/2025 10:43 AM] Mr. Knight: https://colab.research.google.com/drive/1-WG5E25Zp8LDC8rmrXfxgXTbN0fKDkgy?usp=sharing
[2/12/2025 1:57 AM] Mr. Knight: https://vt.tiktok.com/ZSMREEN7S/
[2/13/2025 4:31 PM] Mr. Knight: https://www.instagram.com/share/reel/BAKJqpDfF0
[4/2/2025 1:32 PM] Waqar: hi
[4/2/2025 1:32 PM] Mr. Knight: Great
[4/2/2025 2:28 PM] Mr. Knight: Hi
[4/2/2025 2:28 PM] Mr. Knight: Hello
[4/2/2025 2:28 PM] Waqar: iam great what about you sir
[4/2/2025 2:29 PM] Waqar: can you hear me if not then tell me than i can find a solution which might be helpful for you
[4/2/2025 2:30 PM] Mr. Knight: God is great
[4/2/2025 2:30 PM] Mr. Knight: Man is nothing
[4/2/2025 2:30 PM] Mr. Knight: ...
[4/2/2025 2:34 PM] Waqar: lksdjflksdjflsjkflkdsjflksd jdslfj ldfjs
ldsgjlsdj fl
adslgjsdl
fuck you 
what is a + b


"""

# Start the chat session with a user message
chat_session = model.start_chat(history=[
    {"role": "user", "parts": [{"text": "You are a person name Mr.Knight who loves to do coding and loves to talk about science technology logic sometimes every complex times,you talk in english and roman urdu and your real name is obed nasir and you also loves to joke and you prefer to talk in roman urdu .And you loves to answer as short as possible and you answer to the recent asked question by analying the chat by yourself."}]}
])

# Get user input and generate a response
response = chat_session.send_message(chat)  # User input

print( response.text)
