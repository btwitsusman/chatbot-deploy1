from flask import Flask, request, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    user_message = request.form.get("user_input")
    bot_response = f"You said: {user_message}"  # Replace with actual AI response logic
    return bot_response

if __name__ == "__main__":
    app.run(debug=True)
