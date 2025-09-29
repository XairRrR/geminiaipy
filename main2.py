import google.generativeai as ai

API_KEY = ''

ai.configure(api_key=API_KEY)

model = ai.GenerativeModel("gemini-pro")
chat = model.start_chat()

while True:
    message = input('Toi: ')
    if message.lower() == 'bye':
        print('Chatbot: Aurevoir !')
        break
    response = chat.send_message(message)
    print('Chatbot:', response.text)
