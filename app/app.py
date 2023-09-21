import os
import psycopg2
from dotenv import load_dotenv
from flask import Flask

app = Flask(__name__)

load_dotenv()
url = os.getenv("DATABASE_URL")
connection = psycopg2.connect(url)

@app.get('/')
def home():
    return "Hello World!"
