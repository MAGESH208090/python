from flask import Flask, request, redirect, url_for, render_template, flash
from werkzeug.utils import secure_filename
import os

app = Flask(__name__)
app.secret_key = 'your secret key'

# Allowed file extensions
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/')
def index():
    return render_template('upload.html')

@app.route('/upload', methods=['POST'])
def upload():
    if 'file' not in request.files:
        flash('No file part')
        return redirect(request.url)
    file = request.files['file']
    if file.filename == '':
        flash('No selected file')
        return redirect(request.url)
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        upload_folder = os.path.join(app.instance_path, 'flask_file_upload_example')
        os.makedirs(upload_folder, exist_ok=True)
        file.save(os.path.join(upload_folder, filename))
        flash('File successfully uploaded')
        return redirect(url_for('index'))
    else:
        flash('Allowed file types are txt, pdf, png, jpg, jpeg, gif')
        return redirect(request.url)

if __name__ == '__main__':
    app.run(debug=True)