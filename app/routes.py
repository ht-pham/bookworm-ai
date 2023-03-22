from flask import Flask,render_template, request
from app import bookworm

import openai
openai.api_key = bookworm.OPENAI_API_KEY

from app import app
name = "BookwormAI"

messages = [{"from":name,"text":"Welcome to BookwormAI! I am an AI created by OpenAI."+
            "I am here to help you to get a bite-size summary of your book of interest."
            +"Feel free to give me a book title that you want me to summarize for you."}]

@app.route("/")
def home():
    reload_messages = [{"from":name,"text":"Welcome to BookwormAI! I am an AI created by OpenAI."+
            "I am here to help you to get a bite-size summary of your book of interest."
            +"Feel free to give me a book title that you want me to summarize for you."}]
    return render_template("index.html", name=name,messages=reload_messages)

@app.route('/chat', methods=['POST'])
def chat():
    messages.append({'from':'Human','text':request.form['message']})
    
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt="Summarize the book title: "+request.form['message'],
        temperature=0.9,
        max_tokens=4000,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0.6,
        stop=[" Human:", " AI:"]
    ) 
    answer = response.choices[0].text
    messages.append({"from":name,"text":answer})
    messages.append({"from":name,"text":"Feel free to give me another book title that you want me to summarize for you."})
    
    return render_template("index.html", name=name,messages=messages)

if __name__ == "__main__":
    app.run() 

