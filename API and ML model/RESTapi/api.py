from flask import Flask
import os
import pyttsx3
import ML_bot
from flask import send_file
app = Flask(__name__)

@app.route("/api/getPrediction/<keyword>")
def getResponse(keyword):
    return ML_bot.getResponse(keyword)


@app.route("/api/getAudioText/<keyword>")
def getAudioClip(keyword):
    save_path ="static/output.mp3"
    saveAudioFile(save_path,keyword,100)
    return send_file(os.getcwd()+"/"+save_path)

def saveAudioFile(path,word,rate=100):
    
    engine = pyttsx3.init()
    voices = engine.getProperty('voices') 
    engine.setProperty('rate',rate)
    engine.setProperty('volume',1.0) 
    engine.setProperty('voice', voices[1].id)
    engine.save_to_file(word, path,120)
    engine.runAndWait()
