FROM python:3.11-slim-buster

WORKDIR /app

COPY . .

# install app dependencies
# copied from online after running into warning about ssl certificates
RUN pip install --trusted-host pypi.python.org --trusted-host pypi.org --trusted-host files.pythonhosted.org --trusted-host github.com --trusted-host objects.githubusercontent.com -r requirements.txt

EXPOSE 5000
CMD [ "python", "app.py"]
