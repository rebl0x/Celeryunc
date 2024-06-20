from flask import Flask, request, jsonify
import os
import json
import shutil
app = Flask(__name__)

# Default path for read_file
DEFAULT_PATH = "path to workspace here"
# Function to read a file
def read_file(path):
    full_path = os.path.join(DEFAULT_PATH, path)
    try:
        with open(full_path, 'r') as file:
            content = file.read()
            return content
    except FileNotFoundError:
        return f"File '{full_path}' not found."

# Function to write to a file
def write_file(path, text):
    full_path = os.path.join(DEFAULT_PATH, path)
    try:
        with open(full_path, 'w') as file:
            file.write(text)
            return f"Text written to '{full_path}' successfully."
    except Exception as e:
        return str(e)

def del_file(path):
    full_path = os.path.join(DEFAULT_PATH, path)
    try:
        os.remove(full_path)
        return f"File '{full_path}' deleted successfully."
    except Exception as e:
        return str(e)
        
def create_folder(name):
    full_path = os.path.join(DEFAULT_PATH, name)
    try:
        os.makedirs(full_path, exist_ok=True)
        return f"Folder '{full_path}' created successfully."
    except Exception as e:
        return str(e)

def list_files(name):
    full_path = os.path.join(DEFAULT_PATH, name)
    try:
        files = os.listdir(full_path)
        files_table = json.dumps(files)
        return files_table
    except Exception as e:
        return str(e)
    
       
def del_folder(path):
    full_path = os.path.join(DEFAULT_PATH, path)
    try:
        shutil.rmtree(full_path)
        return f"Folder '{full_path}' deleted successfully."
    except Exception as e:
        return str(e)
        
        
# Route to read a file
@app.route('/readfile', methods=['GET'])
def readfile():
    path = request.args.get('path')
    if not path:
        return jsonify({"error": "Please provide 'path' parameter."}), 400
    content = read_file(path)
    return content

@app.route('/delfile', methods=['GET'])
def delfile():
    path = request.args.get('path')
    if not path:
        return jsonify({"error": "Please provide 'path' parameter."}), 400
    content = del_file(path)
    return content

@app.route('/listfiles', methods=['GET'])
def listfiles():
    path = request.args.get('path')
    if not path:
        return jsonify({"error": "Please provide 'path' parameter."}), 400
    content = list_files(path)
    return content

@app.route('/makefolder', methods=['GET'])
def makefolder():
    name = request.args.get('name')
    if not name:
        return jsonify({"error": "Please provide 'path' parameter."}), 400
    content = create_folder(name)
    return content

@app.route('/delfolder', methods=['GET'])
def delfolder():
    path = request.args.get('path')
    if not path:
        return jsonify({"error": "Please provide 'path' parameter."}), 400
    content = del_folder(path)
    return content

# Route to write to a file
# Route to write to a file using GET request
@app.route('/writefile', methods=['GET'])
def writefile():
    path = request.args.get('path')
    text = request.args.get('text')
    if not path or not text:
        return jsonify({"error": "Please provide 'path' and 'text' parameters."}), 400
    result = write_file(path, text)
    return jsonify({"message": result})


if __name__ == '__main__':
    app.run(debug=True)
