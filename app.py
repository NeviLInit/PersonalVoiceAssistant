from flask import Flask, request, jsonify
from flask_cors import CORS
import subprocess
from root import search_google, open_software, open_website

app = Flask(__name__)
CORS(app)

@app.route('/process_command', methods=['POST'])
def process_command():
    data = request.json
    command = data.get('command')

    if "open my certificate" in command:
        filename1 = r"C:\Users\kalba\Pictures\Screenshots\Harvard certificate.png"
        subprocess.Popen([filename1], shell=True)
        response = "Opening certificate..."
    elif "open browser" in command:
        open_website("http://www.google.com")
        response = "Opening browser..."
    elif "search" in command:
        search_query = command.replace("search", "").strip()
        search_google(search_query)
        response = "Searching..."
    elif "open software" in command:
        software_name = command.replace("open software", "").strip()
        open_software(software_name)
        response = "Opening software..."
    else:
        response = "Command not recognized."

    return jsonify({'response': response})

if __name__ == '__main__':
    app.run(debug=True)