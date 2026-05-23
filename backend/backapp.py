from flask import Flask, jsonify
import mysql.connector
import os

app = Flask(__name__)

@app.route("/")
def home():
    return "Backend container running!"

@app.route("/health")
def health():
    return jsonify({
        "status": "ok",
        "service": "backend"
    }), 200

@app.route("/ready")
def ready():
    try:
        conn = mysql.connector.connect(
            host=os.environ.get("DB_HOST"),
            user=os.environ.get("DB_USER"),
            password=os.environ.get("DB_PASSWORD"),
            database=os.environ.get("DB_NAME")
        )
        conn.close()

        return jsonify({
            "status": "ready",
            "database": "connected"
        }), 200

    except Exception as error:
        return jsonify({
            "status": "not ready",
            "database": "not connected",
            "error": str(error)
        }), 503

@app.route("/db")
def db_check():
    conn = mysql.connector.connect(
        host=os.environ.get("DB_HOST"),
        user=os.environ.get("DB_USER"),
        password=os.environ.get("DB_PASSWORD"),
        database=os.environ.get("DB_NAME")
    )
    conn.close()

    return "Database connection successful!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
