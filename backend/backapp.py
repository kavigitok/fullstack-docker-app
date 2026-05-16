from flask import Flask
import mysql.connector
import os

app = Flask(__name__)

@app.route('/')
def home():
    return "Backend container running!"

@app.route('/db')
def db_check():
    conn = mysql.connector.connect(
        host=os.environ.get("DB_HOST"),
        user=os.environ.get("DB_USER"),
        password=os.environ.get("DB_PASSWORD"),
        database=os.environ.get("DB_NAME")
    )

    return "Database connection successful!"

app.run(host='0.0.0.0', port=5000)
