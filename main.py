from flask import Flask, request, send_file
from rembg import remove
import io

app = Flask(__name__)

@app.route('/')
def home():
    return "Server is Running!"

@app.route('/remove-bg', methods=['POST'])
def remove_bg():
    if 'image_file' not in request.files:
        return {"error": "No file uploaded"}, 400
    
    file = request.files['image_file']
    input_image = file.read()
    output_image = remove(input_image)
    
    return send_file(io.BytesIO(output_image), mimetype='image/png')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
