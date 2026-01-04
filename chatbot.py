from flask import Flask, request, jsonify, render_template
import string
import os

app = Flask(__name__)

# Knowledge base (simple dictionary)
knowledge_base = {
    "hi": "Hello! How can I help you today?",
    "hello": "Hi there! Ask me anything.",
    "hey": "Hey! What would you like to know?",
    "how are you": "I'm doing great! How can I assist you?",
    "good morning": "Good morning! What can I do for you?",
    "good evening": "Good evening! Feel free to ask me something.",
    "good night": "Good night! Take some rest.",
    "thanks": "You're welcome!",

    "who build you": "Anup Shahi built me to assist you.",
    "how to prepare for exams": "Make a timetable and revise regularly.",
    "best programming language to learn": "Start with Python, then JavaScript.",
    "how to improve english": "Read, speak daily, and practice consistently.",
    "what is python": "Python is a backend programming language.",
    "how to build a website": "Learn HTML, CSS, JavaScript, and Flask.",
    "how to create a chatbot": "Use Python with Flask and simple logic."
}

def clean_text(text):
    text = text.lower()
    return text.translate(str.maketrans("", "", string.punctuation)).strip()

@app.route("/")
def index():
    return render_template("index.html")

@app.route('/about-us')
def aboutus(): 
    return render_template('about-us.html')

@app.route("/chat", methods=["POST"])
def chat():
    user_message = request.json.get("message", "")
    cleaned_message = clean_text(user_message)

    # Exact match
    if cleaned_message in knowledge_base:
        return jsonify({"response": knowledge_base[cleaned_message]})

    # Partial match
    for question, answer in knowledge_base.items():
        if question in cleaned_message:
            return jsonify({"response": answer})

    return jsonify({"response": "Sorry, I didn't understand that. Can you rephrase?"})

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=True)