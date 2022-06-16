import requests as rq
from datetime import datetime
import tkinter as tk
import json
import threading
from time import sleep

Nome_Utente = "lixiumu2317"


window = tk.Tk()
window.geometry('600x400')
window.title('Chat by Luca Iaria')
chat_text = ['','','','','','','','','','','','','','','','']
text_chat = ''
old_message= ''
def send_message():
    if username.get():
        global chat, Nome_Utente
        this = tk.Label(window,text='')
        this.grid(row=0,column=1)
        BASE_URL = f'https://{Nome_Utente}.pythonanywhere.com/CHAT'
        payload = {'username':f'{username.get()}','message':f'{message.get()}'}
        response =  rq.get(BASE_URL, params =payload)
        json_values = response.json()
        username_get, message_get, timestamp = json_values['username'], json_values['message'], json_values['timestamp']
        print(f'L\'username: {username_get}')
        print(f'Messagio: {message_get}')
        print(f'Data: {datetime.fromtimestamp(timestamp)}')
    else:
        this = tk.Label(window,text='Attenzione non hai inserito il nome utente!')
        this.grid(row=0,column=1)
def get_messages():
    global chat_text, old_message, Nome_Utente, text_chat
    BASE_URL = f'https://{Nome_Utente}.pythonanywhere.com/CHAT_post'
    response =  rq.get(BASE_URL)
    json_values = response.json()
    username_get, message_get, timestamp = json_values['username'], json_values['message'], json_values['timestamp']
    new_message = f'{datetime.fromtimestamp(timestamp)}, {username_get}: {message_get}'
    if new_message!=old_message:
        chat_text[0] = chat_text[1]
        chat_text[1] = chat_text[2]
        chat_text[2] = chat_text[3]
        chat_text[3] = chat_text[4]
        chat_text[4] = chat_text[5]
        chat_text[5] = chat_text[6]
        chat_text[6] = chat_text[7]
        chat_text[7] = chat_text[8]
        chat_text[8] = chat_text[9]
        chat_text[9] = chat_text[10]
        chat_text[10] = chat_text[11]
        chat_text[11] = chat_text[12]
        chat_text[12] = chat_text[13]
        chat_text[13] = chat_text[14]
        chat_text[14] = chat_text[15]
        chat_text[15] = new_message
        text_chat = ''
        for message in chat_text:
            if message!='':
                text_chat = f'{text_chat}\n{message}'
        old_message=new_message
    chat = tk.Text()
    chat.insert(tk.END,text_chat)
    chat.grid(row=3,column=0,sticky='WE')
    sleep(0.1)
    
username_label = tk.Label(window,text='Username=')
username_label.grid(row=0,column=0,sticky='WN',padx=20,pady=20)
username = tk.Entry()
username.grid(row=0,column=0,sticky='WN',padx=85,pady=20)
message = tk.Entry()
message.grid(row=1,column=0)
invia = tk.Button(text='Invia!',command=send_message)
invia.grid(row=2,column=0)

def infinite_get_messages():
    while True:
        get_messages()
threading.Thread(target=infinite_get_messages).start()
if __name__ == '__main__':
    window.mainloop()
