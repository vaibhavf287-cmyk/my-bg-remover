from flask import Flask, request, send_file
from rembg import remove
import io
import os

app = Flask(__name__)

# Memory bachane ke liye ONNX settings
os.environ["OMP_NUM_THREADS"] = "1"

@app.route('/')
def home():
    return "SERVER IS LIVE"

@app.route('/remove-bg', methods=['POST'])
def remove_bg():
    if 'image_file' not in request.files:
        return "No image file", 400
    
    try:
        file = request.files['image_file']
        input_data = file.read()
        
        # Image process karte waqt memory kam use ho isliye direct return
        output_data = remove(input_data)
        
        return send_file(
            io.BytesIO(output_data),
            mimetype='image/png'
        )
    except Exception as e:
        return str(e), 500

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 10000))
    app.run(host='0.0.0.0', port=port)
0
