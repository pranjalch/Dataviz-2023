from flask import *
from werkzeug.utils import secure_filename
import os, io, json
import pandas as pd
from io import StringIO, BytesIO

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'static'
app.config['MAX_CONTENT_PATH'] = 1024 * 1024

# @app.route("/")
# def hello_world():
#     return "<p>Hello, World! App</p>"

@app.route('/')
def main():
   return render_template('upload.html')

@app.route('/interact', methods = ['POST'])
def uploader():
   if request.method == 'POST':
    #   f = request.files.get('file')
      f = request.files['file']
    #   f.save(os.path.join(app.config['UPLOAD_FOLDER'], secure_filename(f.filename)))
    #   filecontent =  f.fileContents.data
      f.seek(0)
    #   content = StringIO(str(f.read(), 'utf-8'))
      df = pd.read_csv(BytesIO(f.read()))
    #   df_string = df.to_string()

    #   content = TextIOWrapper(f.read())
    #   f.save(secure_filename(f.filename))
      return render_template("interact.html", name = f.filename, data = df.to_html(classes='Data')) 

@app.route('/generative', methods=['POST'])
def generativeai():
    if request.method == 'POST':
        print("Inside generativeai")
        print(request)
        data = request.get_json()
        print(data)
        promt = data[0].get("promt")
        print(promt)
        return promt


if __name__ == '__main__':
   app.run(debug = 'True')