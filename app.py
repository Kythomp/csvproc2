from flask import Flask, request, render_template, redirect, url_for
import os
import csv
import shutil

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    custom_folder_name = request.form['custom_folder']
    destination_folder_path = request.files['destination_folder'].filename
    sorted_photos_folder = os.path.join(destination_folder_path, custom_folder_name)
    
    if not os.path.exists(sorted_photos_folder):
        os.makedirs(sorted_photos_folder)
        print(f"Created folder: {sorted_photos_folder}")

    # Redirect to a new page after processing
    return redirect(url_for('success'))



@app.route('/success')
def success():
    return "Files processed successfully!"

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
