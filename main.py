import os
from dotenv import load_dotenv
from flask import Flask, render_template, request
import openai

# Load .env variables

load_dotenv()
print("Current working directory:", os.getcwd())
print("Env file exists:", os.path.exists('.env'))

# Read Groq key from .env
openai_api_key = os.getenv("OPENAI_API_KEY")

if not openai_api_key:
    print("❌ API KEY NOT LOADED")
else:
    print("✅ API KEY LOADED:", openai_api_key[:8] + "..." + openai_api_key[-4:])

# ✅ Manually assign OpenAI key to OpenAI client
print("Loaded OPENAI_API_KEY:", openai_api_key)
openai.api_key = openai_api_key
openai.api_base = "https://api.groq.com/openai/v1"  # Change this if your API base is different


app = Flask(__name__)

@app.route("/health")
def health():
    """Health check endpoint."""
    return {"status": "ok"}, 200

@app.errorhandler(404)
def page_not_found(e):
    """Custom 404 error page."""
    return render_template("404.html"), 404

@app.route("/")
def index():
    """Render the main page."""
    return render_template("index.html")

@app.route("/fix", methods=["POST"])
def fix():
    """Handle code fixing requests."""
    code = request.form["code"]
    try:
        response = openai.ChatCompletion.create(
            model="llama-3.1-8b-instant",
            messages=[
                {"role": "system", "content": "You are a helpful coding assistant. Fix syntax errors and improve the code."},
                {"role": "user", "content": code}
            ],
            temperature=0.2
        )
        fixed_code = response["choices"][0]["message"]["content"]
        return render_template("index.html", fixed_code=fixed_code, input_code=code)
    except Exception as e:
        error_message = f"An error occurred while processing your code: {str(e)}"
        return render_template("index.html", error=error_message, input_code=code)

if __name__ == "__main__":
    app.run(debug=True)
