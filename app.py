from flask import Flask, request, render_template
from PIL import Image

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    # Get the uploaded file
    file = request.files['file']

    # Open the image using PIL
    img = Image.open(file)

    # Convert the image to grayscale
    img = img.convert('L')

    # Save the grayscale image
    img.save('static/grayscale.jpg')

    # Render the result page
    return render_template('result.html')

if __name__ == '__main__':
    app.run(debug=True)
