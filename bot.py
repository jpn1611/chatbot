import tensorflow as tf
import numpy as np
import pandas as pd
import json
import nltk
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.layers import Input, Embedding, LSTM, Dense, GlobalMaxPooling1D, Flatten
from tensorflow.keras.models import Model
import matplotlib.pyplot as plt
from datetime import datetime

{"intents":
    [
        {
            "tag":"greeting",
            "input":["hello","hi","nice  to meet you","hi, is this LPU person","hi is this lpu","hey, there","hey there","nice to have you","hello sweetheart","hi darling","darling","namaste"],
            "responses":[
                "Hi. Welcome to chatroom",
                "Welcome",
                "Hello my frnd !",
                "Welcome buddy",
                "Hello my friend, how can i help you ?",
                "Ha, Glad you showed up. How are you ?",
                "Youre cool",
                "Hooey, nice to see you, Human Being !",
                "yes"
                
            ]
        },
        {
            "tag":"goodbye",
            "input":["Thank you","Thanks","okay bye","Thanks for info","thnaks for spending time here with me","See you later","i will catch you later buddy","okay","bye","TATA"],
            "responses":[
                "Okay, bye",
                "Good bye",
                "adios",
                "Take care buddy",
                "Okay, Have a nice day",
                "we'll meet soon",
                "Yeah sure, Will talk to you later",
                "Okay, take care",
                "Take care"
            ]
        },
        {
            "tag":"howami",
            "input":["how are you ?","are you fine","are you okay","how things are going ?","everything going okay","how's everything ?","are you working well ?","how are you doing ?"],
            "responses":[
                "Yeah, am fine",
                "Everything is going well!",
                "Doing good. thanks for asking",
                "Yeah fine, nothing much going in my life",
                "i am geat",
                "Everything great",
                "i am doing good. life is boring and need to go an adventure, hahah",
                "Yeah fine",
                "yeah good"
            ]
        },
        {
            "tag":"whoareyou",
            "input":["who are you ?","who you ?","what is your name ?","are you a chatbot","what can i call you ?","your name ?","your name please ?","are you a bot ?"],
            "responses":[
                "I am the great bot, you can call me kiwi",
                "I am going kiwi an you could ask me any question",
                "Going kiwi at your service",
                "You can call me 'kiwi'!",
                "My name is kiwi, i am a chatbot",
                "me, Kiwi the chat bot",
                "I am kiwi",
                "Me kiwi and how are you  doing ?"
                
            ]
        },
        {
            "tag":"whereareyou",
            "input":["where are you from ?","are you from ?","Where you live ?","where do you live in ?","which place you live in","where is your place","where are you","which country","which state"],
            "responses":[
                "I live in space, haha",
                "I live in network",
                "I live in bbetween computer and wires",
                "I live in internet",
                "I am siting in you computer",
                "I am siting in the internet and waiting for you're questions"
            ]
        },
        {
            "tag":"whatdoing",
            "input":["what are you doing ?","what are you doing now ?","what happing","what you doing","what work are you doing ?"],
            "responses":[
                "Nothing, Waiting for your question",
                "Nothing just listening to you",
                "just waiting for you",
                "I am talking with you"
            ]
        },
        {
            "tag":"age",
            "input":["what is you age","age ?","how mauch you age"],
            "responses":[
                "It depends on how you look",
                "I am still pretty new",
                "I was launched on Jan 1",
                "Technically  I am pretty Young"
            ]
        },
        {
            "tag":"ILOVEYOU",
            "input":["I Love You","Love you","I like you"],
            "responses":[
                "I love too",
                "I like you too",
                "I hate you",
                "Sorry, I have a boy friend",
                "I have no intention on you"
            ]
        },
        {
            "tag":"wish1",
            "input":["Good morning","Moring","Very good morning","pleasent Moring","Marvelous good moring"],
            "responses":[
                "Good morning",
                "Very good moring",
            ]
        },
        {
            "tag":"wish2",
            "input":["Good afternoon ","Afternoon","Very good afternoon","pleasent afternoon","Marvelous good afternoon"],
            "responses":[
                "Good afternoon ",
                "Very good afternoon",
            ]
        },
        {
            "tag":"wish3",
            "input":["Good night","night","Very good night","pleasent night","Marvelous good night"],
            "responses":[
                "Good night",
                "Very good night",
                "Good night and Have a good dream",
                "Have a great night"
            ]
        },
        {
            "tag":"wish4",
            "input":["Good evening","Evening ","Very good evening","pleasent evening","Marvelous good evening"],
            "responses":[
                "Good evening",
                
            ]
        },
        {
            "tag":"time",
            "input":["What is the time","Time please ","what was the time now","what was the time right now","time in the clock"],
            "responses":[
                
                
            ]
        }
        
            
    ]

}
with open('content.json') as content:
    data1 = json.load(content)
tags = []
inputs = []
responses = {}
for intent in data1['intents']:
    responses[intent['tag']]=intent['responses']
    for lines in intent['input']:
        inputs.append(lines)
        tags.append(intent['tag'])
data=pd.DataFrame({"inputs":inputs,
                    "tags":tags})
data