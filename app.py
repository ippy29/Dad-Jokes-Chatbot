from flask import Flask, render_template, request
import requests, spacy
from spacytextblob.spacytextblob import SpacyTextBlob

app = Flask(__name__)

# load english language model
nlp = spacy.load("en_core_web_sm") 
# there are a few different versions of this model-> sm is small, therefore faster + less accurate
# can use en_core_web_md and en_core_web_lg too

# pipeline to use for sentiment analysis
nlp.add_pipe("spacytextblob")

@app.route("/")
def home():
    return render_template("index.html")
 
@app.route("/get", methods=['POST', 'GET'])
def get_joke():
    doc = request.get_json()
    doc = doc.get("data")
    if doc == "":
        return "are you going to keep saying nothing?"
    else:
        response = check_sentiment(doc)
        return response

def fetch_joke():
    response = requests.get("https://icanhazdadjoke.com/", verify=False, headers={"Accept": "application/json"})
    # the accept header gets it to return a json response
    #* note that verify=False is insecure and can be removed
    # it was added so that this would work out a dockerfile - could look into installing relevant ca certificates in the dockerfile, but this didn't work for me
    response = response.json().get("joke")
    return response

def check_sentiment(doc):
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