# Voice LLM Interface

A web-based voice interface to interact with a local Ollama LLM. Features an intuitive push-to-talk interface with text-to-speech capabilities.

## Features

- Modern web-based interface with push-to-talk functionality
- Intuitive "hold-to-speak" button with visual feedback
- Real-time speech-to-text using the Web Speech API
- Text-to-speech output for LLM responses
- Customizable voice selection and volume control
- Fallback text input option
- Integration with local Ollama LLM
- Real-time response streaming
- Mobile-friendly design with touch support

## Prerequisites

1. Python 3.8 or higher
2. Ollama installed and running locally
3. A modern web browser (Chrome recommended for best speech features)
4. A working microphone for voice input
5. Speakers or headphones for voice output

## Setup

1. Install Ollama and make sure it's running (default port: 11434)
2. Install the required Python packages:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. Start the web server:
   ```bash
   python voice_interface.py
   ```

2. Open your web browser and navigate to:
   ```
   http://localhost:5000
   ```

3. Voice Input:
   - Press and hold the circular "Hold to Speak" button
   - Speak your message while holding the button
   - Release the button to send your message
   - The button will pulse red while recording

4. Text Input (Alternative):
   - Type your message in the text area
   - Press Enter or click "Send Message" to send

5. Text-to-Speech Settings:
   - Use the checkbox to enable/disable text-to-speech
   - Select your preferred voice from the dropdown menu
   - Adjust the volume using the slider
   - The LLM's responses will be automatically spoken

6. The chat history will appear in the window above.

## Troubleshooting

1. Make sure Ollama is running:
   ```bash
   ollama serve
   ```

2. Ensure the llama2 model is installed:
   ```bash
   ollama pull llama2
   ```

3. Check that your browser has permission to access the microphone
4. If using Chrome, make sure you're using HTTPS or localhost
5. If text-to-speech isn't working:
   - Check that your system volume is on
   - Try selecting a different voice from the dropdown
   - Make sure the text-to-speech checkbox is enabled

6. If push-to-talk isn't working:
   - Make sure you've granted microphone permissions
   - Try refreshing the page
   - Check that no other application is using the microphone
