this project is a chatbot that can be asked to fetch a dad joke from the [icanhazdadjoke](https://icanhazdadjoke.com/) api. it uses the [spaCy](https://pypi.org/project/spacy/) library and Python Flask  

*README last updated:* 14/11/2024  

---

## downloading and running code  
### requirements:  
- Python3.x installed
  - this should work for Python 3.7 to 3.12
  - i used Python 3.11.0b4  
  
### instructions:  
1. copy DadJokesChatbot directory onto local machine
2. set up a python virtual environment:
  - **on Windows** (in command prompt)
  ```
  cd location\of\DadJokesChatbot
  pip install virtualenv
  python -m venv .
  .\Scripts\activate
  ```
3. install required libraries
  `pip install -r requirements.txt`
4. python app.py
  
you should now see something similar to  
  ```
  * Serving Flask app 'app'
  * Debug mode: on
  WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
  * Running on http://127.0.0.1:5000
  Press CTRL+C to quit
  ```  
go to http://127.0.0.1:5000 and you should see the chatbot interface. press CTRL+C in the terminal to quit  
  
run `deactivate` in the terminal to leave virtual environment  

---

## relevant links  
[intro to python virtual environments - freeCodeCamp](https://www.freecodecamp.org/news/how-to-setup-virtual-environments-in-python/)  
[beginners guide to creating a web application with flask - Medium](https://medium.com/@dattu1993/creating-a-web-application-with-python-a-comprehensive-guide-for-beginners-db59df5867e4)  
[html](https://www.w3schools.com/html/), [css](https://www.w3schools.com/css/) and [javascript](https://www.w3schools.com/js/) resources - w3schools  
[python spaCy tutorial - AskPython](https://www.askpython.com/python/examples/chatbot-in-python-using-spacy)  
[jQuery ajax requests](https://api.jquery.com/jQuery.ajax/) resource