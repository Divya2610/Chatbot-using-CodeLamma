# Chatbot-using-CodeLamma
# Q&A Chatbot with Ollama + Gradio

This project is a simple chatbot application built with **Python**, **Gradio**, and **Ollama**.  
It allows you to interact with a locally running Ollama model (e.g., `coder`) through a web interface.

---

## 🚀 Features
- Interactive web-based UI powered by [Gradio](https://gradio.app/).
- Sends prompts to Ollama's API running locally.
- Maintains conversation history during a session.
- Easy to extend with other models (e.g., `llama2`, `mistral`, etc.).

---

## 🛠️ Requirements
- Python 3.9 or above  
- [Ollama](https://ollama.ai/download) installed and running  
- A pulled model in Ollama (example: `coder`)

To pull a model in Ollama:
```bash
ollama pull coder

📦 Setup Instructions

Clone the repository / open your folder

cd section39


Create and activate a virtual environment

python -m venv .venv
# Windows
.venv\Scripts\activate
# macOS/Linux
source .venv/bin/activate


Install dependencies

pip install -r requirements.txt


Or install manually:

pip install requests gradio

▶️ Run the App

Make sure Ollama is running in the background, then start the chatbot:

python app.py


This will launch a Gradio interface at:

http://127.0.0.1:7860

📂 Project Structure
section39/
│── app.py          # Main chatbot code
│── requirements.txt # Dependencies (requests, gradio)
│── README.md        # Project documentation

📝 Example Prompt

Once the UI opens, type a prompt like:

Write a Python function to reverse a string.


And the model will respond inside the browser interface.

🔧 Customization

Change the model in app.py:

"model": "coder"


to any model you have pulled with Ollama (e.g., llama2, mistral).

⚡ Requirements File

Create a requirements.txt with:

requests
gradio


Then install with:

pip install -r requirements.txt

🙌 Acknowledgements

Ollama
 for running local LLMs

Gradio
 for the easy UI


---

👉 Do you want me to also create the `requirements.txt` file for you so you can just `pip install -r requirements.txt`?

You said:
Give me everything in just one go so that i can just copy past 
ChatGPT said:

Got it ✅ I’ll give you everything in one go:

README.md

requirements.txt

Cleaned app.py

So you can just copy-paste and run.

📂 Final Project Files
1. README.md
# Q&A Chatbot with Ollama + Gradio

This project is a simple chatbot application built with **Python**, **Gradio**, and **Ollama**.  
It allows you to interact with a locally running Ollama model (e.g., `coder`) through a web interface.

---

## 🚀 Features
- Interactive web-based UI powered by [Gradio](https://gradio.app/).
- Sends prompts to Ollama's API running locally.
- Maintains conversation history during a session.
- Easy to extend with other models (e.g., `llama2`, `mistral`, etc.).

---

## 🛠️ Requirements
- Python 3.9 or above  
- [Ollama](https://ollama.ai/download) installed and running  
- A pulled model in Ollama (example: `coder`)

Pull a model in Ollama:
```bash
ollama pull coder

📦 Setup Instructions

Open your project folder

cd section39


Create and activate a virtual environment

python -m venv .venv
# Windows
.venv\Scripts\activate
# macOS/Linux
source .venv/bin/activate


Install dependencies

pip install -r requirements.txt

▶️ Run the App

Make sure Ollama is running in the background, then start the chatbot:

python app.py


This will launch a Gradio interface at:

http://127.0.0.1:7860

📂 Project Structure
section39/
│── app.py           # Main chatbot code
│── requirements.txt # Dependencies
│── README.md        # Project documentation

📝 Example Prompt

Once the UI opens, type:

Write a Python function to reverse a string.


And the model will respond inside the browser interface.

🔧 Customization

Change the model in app.py:

"model": "coder"


to any model you have pulled with Ollama (e.g., llama2, mistral).

🙌 Acknowledgements

Ollama
 for running local LLMs

Gradio
 for the easy UI


---

### 2. `requirements.txt`


requests
gradio


---

### 3. `app.py`
```python
import requests
import gradio as gr

url = "http://localhost:11434/api/generate"

headers = {
    "Content-Type": "application/json"
}

history = []

def generate_response(prompt):
    """
    Takes in a user prompt and appends it to the history of prompts.
    It then sends a request to the API with the concatenated history as the prompt.
    If the response is valid, it returns the response from the server.
    If the response is invalid, it prints an error message to the console.
    """
    
    history.append(prompt)
    final_prompt = "\n".join(history)
    data = {
        "model": "coder",     # change this to your Ollama model if needed
        "prompt": final_prompt,
        "stream": False
    }

    response = requests.post(url, headers=headers, json=data)

    if response.status_code == 200:
        result = response.json()
        actual_response = result.get("response", "")
        return actual_response
    else:
        print("error:", response.text)
        return "Error: " + response.text


interface = gr.Interface(
    fn=generate_response,
    inputs=gr.Textbox(lines=4, placeholder="Enter your prompt here..."),
    outputs="text"
)

interface.launch()


✅ Now you just need to:

cd section39
python -m venv .venv
.venv\Scripts\activate   # (Windows) OR source .venv/bin/activate (Linux/Mac)
pip install -r requirements.txt
python app.py
