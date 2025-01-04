from flask import Flask, request, redirect, url_for, render_template, flash
import os
from werkzeug.utils import secure_filename
from flask_wtf import FlaskForm
from wtforms import FileField, SubmitField
from werkzeug.utils import secure_filename

app = Flask(__name__)
app.config['SECRET_KEY'] = "supersecretkey"
app.config['UPLOAD_FOLDER'] = "static/uploads"

class UploadForm(FlaskForm):
    file = FileField("File")
    submit = SubmitField("Upload File")


@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def index():
    form = UploadForm()
    if form.validate_on_submit():
        file = form.file.data
        file.save(os.path.join(os.path.abspath(os.path.dirname(__file__)), app.config['UPLOAD_FOLDER'], secure_filename(file.filename)))
        return "File uploaded successfully"
    
    return render_template('base.html', form=form)


if __name__ == "__main__":
    app.run(debug=True)