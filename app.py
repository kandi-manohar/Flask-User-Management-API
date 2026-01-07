from flask import Flask, render_template, request, jsonify
from db import get_connection

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/users", methods=["POST"])
def create_user():
    data = request.json
    conn = get_connection()
    cur = conn.cursor()
    cur.execute(
        "INSERT INTO user (name, email) VALUES (%s, %s)",
        (data["name"], data["email"])
    )
    conn.commit()
    conn.close()
    return {"message": "User added"}

@app.route("/users", methods=["GET"])
def get_users():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT name, email FROM user")
    users = cur.fetchall()
    conn.close()
    return jsonify(users)

app.run(host="0.0.0.0", port=5000)
