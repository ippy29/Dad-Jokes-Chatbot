from flask import Flask, render_template, request
import requests, spacy, json

app = Flask(__name__)

# load english language model
nlp = spacy.load("en_core_web_md")

@app.route("/")
def home():
    return render_template("index.html")
 
@app.route("/get", methods=['POST', 'GET'])
def get_joke():
    user = request.get_json()
    user = user.get("data")
    response = chatbot(user)
    return response
 
def fetch_joke():
    response = requests.get("https://icanhazdadjoke.com/", headers={"Accept": "application/json"})
    # the accept header gets it to return a json response
    joke = response.json().get("joke")
    return joke

def chatbot(user):
    joke = nlp("dad joke")
    user = nlp(user)
    min_similarity = 0.75
    if joke.similarity(user) >= min_similarity:
        return fetch_joke()
    else:
        response = "try asking for a dad joke"
        return response


if __name__ == "__main__":
    app.run(debug=True)