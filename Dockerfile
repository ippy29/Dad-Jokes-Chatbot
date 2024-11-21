FROM python:3.11-slim-buster

# ENV FLASK_APP=main.py

WORKDIR /app

COPY . .

# install app dependencies
# copied from online after running into warning about ssl certificates
RUN pip install --trusted-host pypi.python.org --trusted-host pypi.org --trusted-host files.pythonhosted.org --trusted-host github.com --trusted-host objects.githubusercontent.com -r requirements.txt

#* installing ca certificates
# download certificates and save them in a directory in dad-jokes-chatbot called ssl
# remove'verify=False, ' from the request to the icanhazdadjokes api in app.py
# uncomment the following lines:
# COPY "ssl/*.crt" "/usr/local/share/ca-certificates/"
# RUN update-ca-certificates

CMD [ "python", "-m" , "flask", "run", "--host=0.0.0.0"]