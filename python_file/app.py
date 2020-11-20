
    #ngrok http -bind-tls=true 5000

from flask import Flask, request
import json

from pers import verify_token
from lyrics import *
from send import envoyer
app=Flask (__name__)    
@app.route('/',methods=['GET']) 
def get_data():
    if (request.args.get('hub.verify_token','')==verify_token) and (request.args.get('hub.mode','')=='subscribe'):
        print("Jetons verifié")
        return (request.args.get('hub.challenge',''))
    else:
        print("Faux jetons")
        return("Votre jetons et")

@app.route('/',methods=['POST'])
def recevoir_message(): 
    data=request.get_json()    
    if data["object"] == "page":      
        for entry in data["entry"]:
            for messaging_event in entry["messaging"]:                
                sender_id = messaging_event["sender"]["id"]         
                if messaging_event.get("message"):                                                                               
                    try:
                        message_text = messaging_event["message"]["text"]
                        print(message_text)
                        donnee=json.dumps(get_results(message_text,sender_id))
                        envoyer(donnee)
                    except KeyError:
                        message_text=None
                                             
    else :
        print("reçu^mais il y avait un bug")          
    return "ok"
if __name__ == "__main__":  
    app.run(debug="True")