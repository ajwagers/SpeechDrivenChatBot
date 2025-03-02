from flask import Flask, render_template, request, jsonify
import requests
import json
import sys
import time

app = Flask(__name__)

class LLMInterface:
    def __init__(self, ollama_url="http://localhost:11434"):
        self.ollama_url = ollama_url
        self.check_ollama_status()
    
    def check_ollama_status(self):
        """Check if Ollama is running and the model is available"""
        try:
            # Check if Ollama service is running
            response = requests.get(f"{self.ollama_url}/api/version")
            response.raise_for_status()
            print("✓ Ollama service is running")
            
            # Check if llama2 model is available
            response = requests.post(
                f"{self.ollama_url}/api/generate",
                json={
                    "model": "llama2",
                    "prompt": "test",
                    "stream": False
                }
            )
            response.raise_for_status()
            print("✓ llama2 model is available")
            return True
            
        except requests.exceptions.ConnectionError:
            print("✗ Error: Cannot connect to Ollama service")
            print("  Please make sure Ollama is installed and running")
            print("  Run 'ollama serve' to start the service")
            sys.exit(1)
        except requests.exceptions.HTTPError as e:
            if "model not found" in str(e).lower():
                print("✗ Error: llama2 model not found")
                print("  Please run 'ollama pull llama2' to download the model")
                sys.exit(1)
            else:
                print(f"✗ Error: {str(e)}")
                sys.exit(1)
        
    def query_ollama(self, text):
        """Send text to Ollama LLM and get response"""
        try:
            response = requests.post(
                f"{self.ollama_url}/api/generate",
                json={
                    "model": "llama2",
                    "prompt": text,
                    "stream": False
                }
            )
            response.raise_for_status()
            return response.json()["response"]
        except requests.exceptions.RequestException as e:
            print(f"Error querying Ollama: {e}")
            return "Sorry, I encountered an error while processing your request."

# Initialize the LLM interface
llm = LLMInterface()

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    data = request.json
    message = data.get('message', '')
    
    if not message:
        return jsonify({'error': 'No message provided'}), 400
    
    response = llm.query_ollama(message)
    return jsonify({'response': response})

if __name__ == '__main__':
    print("Starting Voice LLM Interface...")
    print("Access the web interface at http://localhost:5000")
    app.run(debug=True)
