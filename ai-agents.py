import numpy as np  # For numerical operations
import pandas as pd  # For data manipulation
import openai  # For AI model interactions
import requests  # For making API requests
from transformers import pipeline  # For NLP model processing

class chatAgent:
    def __init__(self,name):
        
        self.name = name

    def greet(self):

        return f"Hello I'm {self.name}, your ai assistant.How can I help you today?"

agent = chatAgent("Saidika")
#print(agent.greet())

def process_input(user_input):

    responses = {
        "hello":"Hello there! How can I assist you today?",
        "bye":"Goodbye!See you later!",
        "help":"I can help with general questions.How can I help you?"
    }

    return responses.get(user_input.lower(),"Sorry, I'm not sure about that,I'm still learning.")

#print(process_input("hey"))

def chat():

    print("Chatbot: Hello! Type 'exit' to end the chat.")

    while True:

        user_input = input("You: ")

        if user_input.lower() == "exit":
            print("Chatbot:Goodbye!See you later!")

            break
        print("Chatbot:", process_input(user_input))

print(chat())