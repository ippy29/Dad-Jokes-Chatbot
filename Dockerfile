FROM python:3.11

# ENV FLASK_APP=main.py

WORKDIR /app

# install app dependencies
# copied from online after running into warning about ssl certificates
COPY requirements.txt requirements.txt
RUN pip install --trusted-host pypi.python.org --trusted-host pypi.org --trusted-host files.pythonhosted.org --trusted-host github.com --trusted-host objects.githubusercontent.com -r requirements.txt

COPY . .

CMD [ "python", "-m" , "flask", "run", "--host=0.0.0.0"]