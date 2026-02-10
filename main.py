from flask import Flask, request, send_file
from rembg import remove
import io

app = Flask(__name__)

@app.route('/')
def home():
    return "SERVER IS LIVE"

@app.route('/remove-bg', methods=['POST'])
def remove_bg():
    # Hum check kar rahe hain ki 'image_file' naam ka data aaya ya nahi
    if 'image_file' not in request.files:
        return "No image_file found in request", 400
    
    try:
        file = request.files['image_file']
        input_image = file.read()
        output_image = remove(input_image)
        return send_file(io.BytesIO(output_image), mimetype='image/png')
    except Exception as e:
        return str(e), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
