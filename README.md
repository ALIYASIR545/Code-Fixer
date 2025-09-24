<<<<<<< HEAD

![MIT License](https://img.shields.io/badge/license-MIT-green)

# CodeFixer (LLAMA 3.1)

A web app to fix and improve code using LLAMA 3.1 via the OpenAI-compatible API.

## Features
- Paste buggy code and get instant fixes
- Supports syntax and logic improvements
- Stylish, responsive UI with dark mode
- Copy-to-clipboard and error handling


## Usage
Paste your buggy code, click "Fix My Code", and get an improved version instantly. Supports Python, Java, and more.

## Setup Instructions

1. **Clone the repository:**
   ```sh
   git clone <your-repo-url>
   cd codefixer
   ```

2. **Create a virtual environment (recommended):**
   ```sh
   python -m venv venv
   # On Windows:
   venv\Scripts\activate
   # On Mac/Linux:
   source venv/bin/activate
   ```

3. **Install dependencies:**
   ```sh
   pip install -r requirements.txt
   ```

4. **Add your API key:**
   - Create a file named `.env` in the project root.
   - Add this line (replace with your actual key):
     ```
     OPENAI_API_KEY=your_actual_api_key_here
     ```

5. **Run the app:**
   ```sh
   python main.py
   ```
   Then open [http://127.0.0.1:5000/](http://127.0.0.1:5000/) in your browser.

## Notes
- Your `.env` file is ignored by git for security.
- If you want to deploy, use a production WSGI server (not Flask’s built-in server).
- For Groq or other OpenAI-compatible APIs, make sure the `openai.api_base` in `main.py` is set correctly.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
=======
# Code-Fixer
>>>>>>> 8b1674fb628bc54665e26586c67710b249c5aaca
