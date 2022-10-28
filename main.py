from tkinter import *
from chatterbot impor
t ChatBot
from chatterbot.trainers import ListTrainer
import os
import pyttsx3
import speech_recognition
import threading
bot = ChatBot('bot')
trainer=ListTrainer(bot)
data_list= [ 'What is the capital of India',
            'Delhi is the capital of India',
            'In which language you talk',
            'I mostly talk in english',
            'What you do in free time',
            'I memorize things in my free time',
            'Ok bye',
            'bye take care' ]


for files in os.listdir('data/english/'):
    data=open('data/english/'+files,'r',encoding='utf-8').readlines()

trainer.train(data_list)

def botReply():
    question=questionField.get()
    question=question.capitalize()
    answer=bot.get_response(question)
    textarea.insert(END,'You: '+question+'\n\n')
    textarea.insert(END,'Bot: '+str(answer)+'\n\n')
    pyttsx3.speak(answer)
    questionField.delete(0,END)

def audioText():
    while True:
        sr=speech_recognition.Recognizer()
        try:
            with speech_recognition.Microphone()as m:
                sr.adjust_for_ambient_noise(m,duration=0.2)
                audio= sr.listen(m)
                query =sr.recognize_google(audio)

                questionField.delete(0,END)
                questionField.insert(0,query)
        except Exception as e:
            print(e)
root=Tk()

root.geometry('500x570+100+30')
root.title('ChatBot created by Team 6')
root.config(bg='deep pink')

logoPic=PhotoImage(file='pic.png')

logoPicLabel=Label(root,image=logoPic,bg='deep pink')
logoPicLabel.pack(pady=5)

centerFrame=Frame(root)
centerFrame.pack()

scrollbar=Scrollbar(centerFrame)
scrollbar.pack(side=RIGHT)

textarea=Text(centerFrame,font=('times new roman',20,'bold'),height=10,yscrollcommand=scrollbar.set
              ,wrap='word')
textarea.pack(side=LEFT)
scrollbar.config(command=textarea.yview)

questionField=Entry(root,font=('verdana',20,'bold'))
questionField.pack(pady=15,fill=X)

askPic=PhotoImage(file='ask.png')


askButton=Button(root,image=askPic,command=botReply)
askButton.pack()

def click(event):
    askButton.invoke()


root.bind('<Return>',click)

thread= threading.Thread(target=audioText)
thread.setDaemon(True)
thread.start()
root.mainloop()