from flask import Flask, request, jsonify, redirect, url_for
import json
import os 

app = Flask(__name__)

# data storage
DATA_FILE = "users.json"

def load_users():
    if not os.path.exists(DATA_FILE):
        return []
    with open(DATA_FILE, "r") as f:
        return json.load(f)

def save_users(users):
    with open(DATA_FILE, "w") as f:
        json.dump(users, f)

users = load_users()

@app.route("/")
def home():
    return """
    <h2>Login</h2>
    <form action="/login" method="post">
        Email: <input name="email"><br>
        Password: <input name="password"><br>
        <button type="submit">Login</button>
    </form>

    <p>Belum punya akun?</p>
    <a href="/register-page">Register di sini</a>
    """

@app.route("/register-page")
def register_page():
    return """
    <h2>Register</h2>
    <form action="/register" method="post">
        Email: <input name="email"><br>
        Password: <input name="password"><br>
        <button type="submit">Register</button>
    </form>

    <p>Sudah punya akun?</p>
    <a href="/">Login di sini</a>
    """

# API 
# REGISTER
@app.route("/register", methods=["POST"])
def register():
    data = request.form or request.json

    email = data.get("email")
    password = data.get("password")

    # bersihin spasi
    if email:
        email = email.strip()
    if password:
        password = password.strip()

    if not email or not password:
        return jsonify({"error": "Email dan password wajib diisi"}), 400

    if len(password) < 6:
        return jsonify({"error": "Password minimal 6 karakter"}), 400

    for user in users:
        if user["email"] == email:
            return jsonify({"error": "Email sudah terdaftar"}), 400

    users.append({"email": email, "password": password})

    # kalau dari browser
    if request.form:
        return redirect(url_for("profile"))

    return jsonify({"message": "User registered"}), 201

# LOGIN
@app.route("/login", methods=["POST"])
def login():
    data = request.form or request.json

    for user in users:
        if user["email"] == data.get("email") and user["password"] == data.get("password"):
            
            if request.form:
                return redirect(url_for("profile"))

            return jsonify({"message": "Login success"}), 200

    return jsonify({"error": "Login gagal"}), 401


# PROFILE
@app.route("/profile")
def profile():
    user_list = "<br>".join([u["email"] for u in users])
    return f"""
    <h2>Profile Page</h2>
    <p>Users:</p>
    {user_list}
    <br><br>
    <a href="/">Logout</a>
    """


if __name__ == "__main__":
    app.run(debug=True)


