import os
import urllib.request
from flask import Flask, render_template, flash, request, redirect, url_for
from werkzeug.utils import secure_filename
from flask import send_from_directory
import tempfile
import uuid
import io
import subprocess

from process import textualize
from text2speech import speak



UPLOAD_FOLDER = 'static/uploads'
ALLOWED_EXTENSIONS = {'mp4'} #todo: support for mp3 files

app = Flask(__name__)
app.secret_key = "secret key"
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 200 * 1024 * 1024

def addDialect(lang):
	if lang=="en":
		return "en-CA"
	if lang=="fr":
		return "fr-CA"
	if lang=="hi":
		return "hi-IN"
	if lang=="ja":
		return "ja-JP"
	if lang=="es":
		return "es-ES"
	if lang=="zh":
		return "cmn-CN"


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/uploads/<filename>')
def send_file(filename):
    return send_from_directory(UPLOAD_FOLDER, filename)

@app.route('/process/<input>/<output>/<filename>')
def process_file(input, output, filename):
    print(url_for('send_file', filename = filename))
    #data = ("bonjour", "hello")
    data = textualize(os.path.join(app.config['UPLOAD_FOLDER'], filename), input_lang = input, target_lang = output)
    orig_text= data[0]
    trans_text = data[1]
    audiofile = uuid.uuid4().hex +".mp3"
    propername = os.path.join(app.config['UPLOAD_FOLDER'], audiofile)
    subprocess.check_call(['./dub.sh', os.path.join(app.config['UPLOAD_FOLDER'], filename), propername])
    print("GOT HERE:::" + propername)
    speak(trans_text, addDialect(output), propername)
    return render_template('play.html', filename = "uploads/"+audiofile, orig = orig_text, trans = trans_text, input = input, output = output)

#@app.route('/play/<input>/<output>/<filename>')
#def uploaded_file(filename, lang):
#    return redirect(url_for('process_file', filename = filename, lang=lang))

@app.route('/', methods=['GET','POST'])
def upload_file():
    if request.method == 'POST':
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return redirect(url_for('process_file', filename=filename, input=request.form['input'], output=request.form['output']))
    return render_template('index.html')

if __name__ == '__main__':
    # This is used when running locally only. When deploying to Google App
    # Engine, a webserver process such as Gunicorn will serve the app. This
    # can be configured by adding an `entrypoint` to app.yaml.
    # Flask's development server will automatically serve static files in
    # the "static" directory. See:
    # http://flask.pocoo.org/docs/1.0/quickstart/#static-files. Once deployed,
    # App Engine itself will serve those files as configured in app.yaml.
    app.run(host='127.0.0.1', port=8080, debug=True)


