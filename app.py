from flask import Flask, render_template, request
import requests, spacy
from spacy.matcher import Matcher
from spacytextblob.spacytextblob import SpacyTextBlob

app = Flask(__name__)

# load english language model
nlp = spacy.load("en_core_web_md")

nlp.add_pipe("spacytextblob")

@app.route("/")
def home():
    return render_template("index.html")
 
@app.route("/get", methods=['POST', 'GET'])
def get_joke():
    doc = request.get_json()
    doc = doc.get("data")
    response = chatbot(doc)
    return response
 
def fetch_joke():
    response = requests.get("https://icanhazdadjoke.com/", headers={"Accept": "application/json"})
    # the accept header gets it to return a json response
    response = response.json().get("joke")
    return response

def chatbot(doc):
    doc = nlp(doc)
    sentiment = doc._.blob.polarity
    sentiment = round(sentiment, 2)
    if sentiment >= 0.5:
        friendlyHtml = "<br><b>mr. bot:</b> ⸂⸂⸜(രᴗര๑)⸝⸃⸃"
        return (check_for_joke(doc) + friendlyHtml) 
    elif sentiment >= 0:
        return check_for_joke(doc) 
    else:
        response = "do you not like me :("
        return response

def check_for_joke(doc):
    joke = nlp("joke")
    min_similarity = 0.7
    if joke.similarity(doc) >= min_similarity:
        return fetch_joke()
    else:
        response = "try asking for a dad joke!"
        return response

if __name__ == "__main__":
    app.run(debug=True)