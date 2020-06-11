from flask import Flask
from bs4 import BeautifulSoup as BS
import requests as req

req = req.get('http://mk.ru/anekdoti')

soup = BS(req.text, 'lxml')
app = Flask(__name__)


@app.route('/')
def index():
    for i in range(0, 4):
        jokes = soup.find_all('p','text')
        for i in range(0, 4):
            result_str = ''
            for item in range(0, 4):
                result_str+='<br>'+ jokes.pop(0).text
            return result_str
if __name__ == "__main__":
    app.run(debug=True)
