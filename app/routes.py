from flask import Flask,render_template, request
from app import app
from app.chatbot import Chatbot

name = "BookwormAI"
ai_engine = Chatbot()
messages = [{"from":name,"text":ai_engine.introduce()}]

@app.route("/")
def home():
    # When the home page is (re)loaded
    reload_messages = messages
    return render_template("index.html", name=name,messages=reload_messages)

@app.route('/chat', methods=['POST'])
def chat():
    # Get the book title from the user
    messages.append({'from':'Human','text':request.form['message']})

    # Process the request from the user
    ai_engine.receiveBooktitle(request.form['message'])
    answer = ai_engine.processRequest()

    # Return the summary to the user and auto reply to the user
    messages.append({"from":name,"text":answer})
    messages.append({"from":name,"text":ai_engine.autoReply()})
    
    return render_template("index.html", name=name,messages=messages)

if __name__ == "__main__":
    app.run() 

