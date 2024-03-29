from flask import Flask, render_template
from flask import Flask
import src.predict  as p
import os
from flask import Flask, render_template, request
from werkzeug.utils import secure_filename
from flask import send_from_directory



app = Flask(__name__)

app.config['UPLOAD_FOLDER'] = '/home/maria/Documents/final-project/fotos'

@app.route('/fotos/<path:path>')
def send_js(path):   
 return send_from_directory('fotos', path)

@app.route("/")
def upload_file():
 return render_template('index.html')

@app.route("/upload", methods=['POST'])
def uploader():
  if request.method == 'POST': 
    f = request.files['archivo']
    filename = secure_filename(f.filename)

    #f.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
    #prediction = p.get_prediction(os.path.join(app.config['UPLOAD_FOLDER'], filename))
    image = f.save("/home/maria/Documents/final-project/fotos/predict.jpg")
    pred = p.get_prediction("/home/maria/Documents/final-project/fotos/predict.jpg")
    return render_template("predict.html",pred=pred )

if __name__ == '__main__':

 app.run(debug=True)